import copy
from dbdicom.record import DbRecord

class Database(DbRecord):

    def loc(self):
        df = self.manager.register
        return df.removed==False

    def _set_key(self):
        if not self.manager.register.empty:
            self._key = self.manager.register.index[0]
        else:
            self._key = None

    def parent(self):
        return

    def children(self, **kwargs):
        return self.patients(**kwargs)

    def new_child(self, dataset=None, **kwargs): 
        attr = {**kwargs, **self.attributes}
        return self.new_patient(**attr)

    def save(self, path=None):
        #self.manager.save('Database')
        self.manager.save()
        self.write(path)

    def restore(self, path=None):
        self.manager.restore()
        self.write(path)

    def open(self, path):
        self.manager.open(path)

    def close(self):
        return self.manager.close()

    def scan(self):
        self.manager.scan()

    def import_dicom(self, files):
        self.manager.import_datasets(files)

    def _copy_from(self, record):
        uids = self.manager.copy_to_database(record.uid, **self.attributes)
        if isinstance(uids, list):
            return [self.record('Patient', uid) for uid in uids]
        else:
            return self.record('Patient', uids)

    def zeros(*args, **kwargs):
        return zeros(*args, **kwargs)

def zeros(database, shape, dtype='mri'):
    study = database.new_study()
    return study.zeros(shape, dtype=dtype)



