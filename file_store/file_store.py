from .key_value_item import KeyValueItem
import os
import logging

logger = logging.getLogger(__name__)

# FileStore is a simple key-value store that persists data to the file system.
class FileStore:
    def __init__(self, root_path):
        self.root_path = root_path
        # create the root path if it does not exist
        if not os.path.exists(root_path):
            os.makedirs(root_path)

        # preload index

    def keys(self):
        return os.listdir(self.root_path)

    def get(self, key):
        return KeyValueItem(os.path.join(self.root_path, key)).read()

    def insert(self, key, value, safe=True):
        if self.key_exists(key): 
            logger.debug(f"Key {key} already exists")
            # safe is true, make a copy of the old file with a suffix version
            if safe:
                old_file_path = os.path.join(self.root_path, key)
                file = KeyValueItem(old_file_path).bump_version() 
                os.rename(old_file_path, str(file))
            else:
                raise ValueError(f"Key {key} already exists")
        self.save(key, value)

    def save(self, key, value):
        with open(os.path.join(self.root_path, key), 'w') as f:
            f.write(value)

    def delete(self, key):
        os.remove(os.path.join(self.root_path, key))

    def clear(self):
        for key in self.keys():
            self.delete(key)

    def key_exists(self, key):
        # check if file exists
        return os.path.exists(os.path.join(self.root_path, key))
        # if keys are indexed, use the follow implementation
        #return key in self.keys()

    def destroy(self):
        self.clear()
        os.rmdir(self.root_path)