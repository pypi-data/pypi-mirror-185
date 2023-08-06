import os
import math

import numpy as np

from dbdicom.record import DbRecord
from dbdicom.ds import MRImage
import dbdicom.utils.image as image_utils
import dbdicom.utils.scipy as scipy_utils


class Series(DbRecord):

    name = 'SeriesInstanceUID'

    def _set_key(self):
        self._key = self.keys()[0]

    def remove(self):
        self.manager.delete_series([self.uid])

    def parent(self):
        uid = self.manager.register.at[self.key(), 'StudyInstanceUID']
        return self.record('Study', uid, key=self.key())

    def children(self, **kwargs):
        return self.instances(**kwargs)

    def new_child(self, dataset=None, **kwargs): 
        attr = {**kwargs, **self.attributes}
        return self.new_instance(dataset=dataset, **attr)

    def new_instance(self, dataset=None, **kwargs):
        attr = {**kwargs, **self.attributes}
        uid, key = self.manager.new_instance(parent=self.uid, dataset=dataset, key=self.key(), **attr)
        return self.record('Instance', uid, key, **attr)

    # replace by clone(). Adopt implies move rather than copy
    def adopt(self, instances): 
        uids = [i.uid for i in instances]
        uids = self.manager.copy_to_series(uids, self.uid, **self.attributes)
        if isinstance(uids, list):
            return [self.record('Instance', uid) for uid in uids]
        else:
            return self.record('Instance', uids)        

    def _copy_from(self, record, **kwargs):
        attr = {**kwargs, **self.attributes}
        uids = self.manager.copy_to_series(record.uid, self.uid, **attr)
        if isinstance(uids, list):
            return [self.record('Instance', uid) for uid in uids]
        else:
            return self.record('Instance', uids)

    def affine_matrix(self):
        return affine_matrix(self)

    def array(*args, **kwargs):
        return get_pixel_array(*args, **kwargs)

    def set_array(*args, **kwargs):
        set_pixel_array(*args, **kwargs)

    def map_to(*args, **kwargs):
        return scipy_utils.map_to(*args, **kwargs)

    def map_mask_to(*args, **kwargs):
        return scipy_utils.map_mask_to(*args, **kwargs)

    def export_as_npy(*args, **kwargs):
        export_as_npy(*args, **kwargs)

    def subseries(*args, move=False, **kwargs):
        return subseries(*args, move=move, **kwargs)

    def import_dicom(*args, **kwargs):
        import_dicom(*args, **kwargs)

    #
    # Following APIs are obsolete and will be removed in future versions
    #

    # Obsolete - use array()
    def get_pixel_array(*args, **kwargs): 
        return get_pixel_array(*args, **kwargs)

    # Obsolete - use set_array()
    def set_pixel_array(*args, **kwargs):
        set_pixel_array(*args, **kwargs)



def import_dicom(series, files):
    uids = series.manager.import_datasets(files)
    series.manager.move_to(uids, series.uid)

def subseries(record, move=False, **kwargs):
    """Extract subseries"""
    series = record.new_sibling()
    for instance in record.instances(**kwargs):
        if move:
            instance.move_to(series)
        else:
            instance.copy_to(series)
    # This should be faster:
    # instances = record.instances(**kwargs)
    # series.adopt(instances)
    return series

def read_npy(record):
    # Not in use - loading of temporary numpy files
    file = record.manager.npy()
    if not os.path.exists(file):
        return
    with open(file, 'rb') as f:
        array = np.load(f)
    return array

def export_as_npy(record, directory=None, filename=None, sortby=None, pixels_first=False):
    """Export array in numpy format"""

    if directory is None: 
        directory = record.dialog.directory(message='Please select a folder for the png data')
    if filename is None:
        filename = record.SeriesDescription
    array, _ = record.get_pixel_array(sortby=sortby, pixels_first=pixels_first)
    file = os.path.join(directory, filename + '.npy')
    with open(file, 'wb') as f:
        np.save(f, array)

def affine_matrix(series):
    """Returns the affine matrix of a series.
    
    If the series consists of multiple slice groups with different 
    image orientations, then a list of affine matrices is returned,
    one for each slice orientation.
    """
    image_orientation = series.ImageOrientationPatient
    # Multiple slice groups in series - return list of affine matrices
    if isinstance(image_orientation[0], list):
        affine_matrices = []
        for dir in image_orientation:
            slice_group = series.instances(ImageOrientationPatient=dir)
            mat = _slice_group_affine_matrix(slice_group, dir)
            affine_matrices.append(mat)
        return affine_matrices
    # Single slice group in series - return a single affine matrix
    else:
        slice_group = series.instances()
        return _slice_group_affine_matrix(slice_group, image_orientation)


def _slice_group_affine_matrix(slice_group, image_orientation):
    """Return the affine matrix of a slice group"""

    # single slice
    if len(slice_group) == 1:
        return slice_group[0].affine_matrix
    # multi slice
    else:
        image_position_patient = [s.ImagePositionPatient for s in slice_group]
        if len(image_position_patient) == 1: 
            return slice_group[0].affine_matrix
        # Slices with different locations
        else:
            return image_utils.affine_matrix_multislice(
                image_orientation,
                image_position_patient,
                slice_group[0].PixelSpacing)    # assume all the same pixel spacing



def get_pixel_array(record, sortby=None, pixels_first=False): 
    """Pixel values of the object as an ndarray
    
    Args:
        sortby: 
            Optional list of DICOM keywords by which the volume is sorted
        pixels_first: 
            If True, the (x,y) dimensions are the first dimensions of the array.
            If False, (x,y) are the last dimensions - this is the default.

    Returns:
        An ndarray holding the pixel data.

        An ndarry holding the datasets (instances) of each slice.

    Examples:
        ``` ruby
        # return a 3D array (z,x,y)
        # with the pixel data for each slice
        # in no particular order (z)
        array, _ = series.array()    

        # return a 3D array (x,y,z)   
        # with pixel data in the leading indices                               
        array, _ = series.array(pixels_first = True)    

        # Return a 4D array (x,y,t,k) sorted by acquisition time   
        # The last dimension (k) enumerates all slices with the same acquisition time. 
        # If there is only one image for each acquision time, 
        # the last dimension is a dimension of 1                               
        array, data = series.array('AcquisitionTime', pixels_first=True)                         
        v = array[:,:,10,0]                 # First image at the 10th location
        t = data[10,0].AcquisitionTIme      # acquisition time of the same image

        # Return a 4D array (loc, TI, x, y) 
        sortby = ['SliceLocation','InversionTime']
        array, data = series.array(sortby) 
        v = array[10,6,0,:,:]            # First slice at 11th slice location and 7th inversion time    
        Loc = data[10,6,0][sortby[0]]    # Slice location of the same slice
        TI = data[10,6,0][sortby[1]]     # Inversion time of the same slice
        ```  
    """
    if sortby is not None:
        if not isinstance(sortby, list):
            sortby = [sortby]
    source = instance_array(record, sortby)
    array = []
    instances = source.ravel()
    for i, im in enumerate(instances):
        record.progress(i, len(instances), 'Reading pixel data..')
        if im is None:
            array.append(np.zeros((1,1)))
        else:
            array.append(im.get_pixel_array())
    record.status.hide()
    array = _stack(array)
    array = array.reshape(source.shape + array.shape[1:])
    if pixels_first:
        array = np.moveaxis(array, -1, 0)
        array = np.moveaxis(array, -1, 0)
    return array, source 


def set_pixel_array(series, array, source=None, pixels_first=False): 
    """
    Set pixel values of a series from a numpy ndarray.

    Since the pixel data do not hold any information about the 
    image such as geometry, or other metainformation,
    a dataset must be provided as well with the same 
    shape as the array except for the slice dimensions. 

    If a dataset is not provided, header info is 
    derived from existing instances in order.

    Args:
        array: 
            numpy ndarray with pixel data.

        dataset: 
            numpy ndarray

            Instances holding the header information. 
            This *must* have the same shape as array, minus the slice dimensions.

        pixels_first: 
            bool

            Specifies whether the pixel dimensions are the first or last dimensions of the series.
            If not provided it is assumed the slice dimensions are the last dimensions
            of the array.

        inplace: 
            bool

            If True (default) the current pixel values in the series 
            are overwritten. If set to False, the new array is added to the series.
    
    Examples:
        ```ruby
        # Invert all images in a series:
        array, _ = series.array()
        series.set_array(-array)

        # Create a maximum intensity projection of the series.
        # Header information for the result is taken from the first image.
        # Results are saved in a new sibling series.
        array, data = series.array()
        array = np.amax(array, axis=0)
        data = np.squeeze(data[0,...])
        series.new_sibling().set_array(array, data)

        # Create a 2D maximum intensity projection along the SliceLocation direction.
        # Header information for the result is taken from the first slice location.
        # Current data of the series are overwritten.
        array, data = series.array('SliceLocation')
        array = np.amax(array, axis=0)
        data = np.squeeze(data[0,...])
        series.set_array(array, data)

        # In a series with multiple slice locations and inversion times,
        # replace all images for each slice location with that of the shortest inversion time.
        array, data = series.array(['SliceLocation','InversionTime']) 
        for loc in range(array.shape[0]):               # loop over slice locations
            slice0 = np.squeeze(array[loc,0,0,:,:])     # get the slice with shortest TI 
            TI0 = data[loc,0,0].InversionTime           # get the TI of that slice
            for TI in range(array.shape[1]):            # loop over TIs
                array[loc,TI,0,:,:] = slice0            # replace each slice with shortest TI
                data[loc,TI,0].InversionTime = TI0      # replace each TI with shortest TI
        series.set_array(array, data)
        ```
    """

    if pixels_first:    # Move to the end (default)
        array = np.moveaxis(array, 0, -1)
        array = np.moveaxis(array, 0, -1)

    # if no header data is provided, use template headers.
    # Note - looses information on dimensionality of array
    # Everything is reduced to 3D
    if source is None:
        if array.ndim <= 2:
            n = 1
        else:
            n = np.prod(array.shape[:-2])
        source = np.empty(n, dtype=object)
        for i in range(n): 
            source[i] = series.new_instance(MRImage())  
        if array.ndim > 2:
            source = source.reshape(array.shape[:-2])
        set_pixel_array(series, array, source)
        #source = instance_array(series)

    # Return with error message if dataset and array do not match.
    nr_of_slices = int(np.prod(array.shape[:-2]))
    if nr_of_slices != np.prod(source.shape):
        message = 'Error in set_array(): array and source do not match'
        message += '\n Array has ' + str(nr_of_slices) + ' elements'
        message += '\n Source has ' + str(np.prod(source.shape)) + ' elements'
        series.dialog.error(message)
        raise ValueError(message)

    # Flatten array and source for iterating
    array = array.reshape((nr_of_slices, array.shape[-2], array.shape[-1])) # shape (i,x,y)
    source = source.reshape(nr_of_slices).tolist() # shape (i,)

    # set_array replaces current array
    # -> remove all instances not in the source
    instances = series.instances()
    for i in series.instances():
        if i not in source:
            i.remove()

    # Any sources currently not in the series
    # -> replace by a copy in the series
    instances = series.instances()
    copy_source = []
    for i, s in enumerate(source):
        series.status.progress(i+1, len(source), 'Saving array (1/2): Copying series..')
        if s in instances:
            copy_source.append(s)
        else:
            copy_source.append(s.copy_to(series))
    # if series.instances() == []:
    #     copy = copy_to(source.tolist(), series)
    # else:
    #     copy = source.tolist()

    series.manager.pause_extensions()
    for i, s in enumerate(copy_source):
        series.status.progress(i+1, len(copy_source), 'Saving array (2/2): Writing array..')
        s.set_pixel_array(array[i,...])
    series.manager.resume_extensions()

    # Then replace array
    # series.manager.pause_extensions()
    # for i, instance in enumerate(copy):
    #     series.status.progress(i+1, len(copy), 'Writing array to file..')
    #     instance.set_pixel_array(array[i,...])
    # series.manager.resume_extensions()


    # More compact but does not work with pause extensions
    # series.manager.pause_extensions()
    # for i, s in enumerate(source):
    #     series.status.progress(i+1, len(source), 'Writing array..')
    #     if s not in instances:
    #         s.copy_to(series).set_pixel_array(array[i,...])
    #     else:
    #         s.set_pixel_array(array[i,...])
    # series.manager.resume_extensions()





##
## Helper functions
##


def instance_array(record, sortby=None, status=True): 
    """Sort instances by a list of attributes.
    
    Args:
        sortby: 
            List of DICOM keywords by which the series is sorted
    Returns:
        An ndarray holding the instances sorted by sortby.
    """
    if sortby is None:
        instances = record.instances()
        array = np.empty(len(instances), dtype=object)
        for i, instance in enumerate(instances): 
            array[i] = instance
        return array
    else:
        df = record.read_dataframe(sortby + ['SOPInstanceUID'])
        # if set(sortby) <= set(record.manager.register):
        #     df = record.manager.register.loc[dataframe(record).index, sortby]  # obsolete replace by below
        #     # df = record.manager.register.loc[record.register().index, sortby]
        # else:
        #     ds = record.get_dataset()
        #     df = dbdataset.get_dataframe(ds, sortby)
        df.sort_values(sortby, inplace=True) 
        return df_to_sorted_instance_array(record, df, sortby, status=status)

# def dataframe(record): # OBSOLETE replace by record.register()

#     keys = record.manager.keys(record.uid)
#     return record.manager.register.loc[keys, :]


def df_to_sorted_instance_array(record, df, sortby, status=True): 

    data = []
    vals = df[sortby[0]].unique()
    for i, c in enumerate(vals):
        if status: 
            record.progress(i, len(vals), message='Sorting..')
        dfc = df[df[sortby[0]] == c]
        if len(sortby) == 1:
            datac = df_to_instance_array(record, dfc)
        else:
            datac = df_to_sorted_instance_array(record, dfc, sortby[1:], status=False)
        data.append(datac)
    return _stack(data, align_left=True)


def df_to_instance_array(record, df): 
    """Return datasets as numpy array of object type"""

    data = np.empty(df.shape[0], dtype=object)
    # for i, uid in enumerate(df.SOPInstanceUID.values): 
    #     data[i] = record.instance(uid)
    #for i, item in enumerate(df.SOPInstanceUID.items()): 
    for i, item in enumerate(df.SOPInstanceUID.items()):
        #data[i] = record.instance(item[1], item[0])
        data[i] = record.instance(key=item[0])
    return data

def _stack(arrays, align_left=False):
    """Stack a list of arrays of different shapes but same number of dimensions.
    
    This generalises numpy.stack to arrays of different sizes.
    The stack has the size of the largest array.
    If an array is smaller it is zero-padded and centred on the middle.
    """

    # Get the dimensions of the stack
    # For each dimension, look for the largest values across all arrays
    ndim = len(arrays[0].shape)
    dim = [0] * ndim
    for array in arrays:
        for i, d in enumerate(dim):
            dim[i] = max((d, array.shape[i])) # changing the variable we are iterating over!!
    #    for i in range(ndim):
    #        dim[i] = max((dim[i], array.shape[i]))

    # Create the stack
    # Add one dimension corresponding to the size of the stack
    n = len(arrays)
    #stack = np.full([n] + dim, 0, dtype=arrays[0].dtype)
    stack = np.full([n] + dim, None, dtype=arrays[0].dtype)

    for k, array in enumerate(arrays):
        index = [k]
        for i, d in enumerate(dim):
            if align_left:
                i0 = 0
            else: # align center and zero-pad missing values
                i0 = math.floor((d-array.shape[i])/2)
            i1 = i0 + array.shape[i]
            index.append(slice(i0,i1))
        stack[tuple(index)] = array

    return stack

