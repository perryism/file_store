from file_store import FileStore

import unittest

class TestFileKeyStore(unittest.TestCase):
    def setUp(self):
        self.store = FileStore("/tmp/test_file_key_store")

    def tearDown(self):
        self.store.destroy()

    def test_save_value(self):
        self.store.insert("key", "value")
        self.assertEqual(self.store.get("key"), "value")

        self.store.insert("key2", "value2")
        self.store.insert("key2", "value3")

        self.assertEqual(len(self.store.keys()), 3)

    def test_delete_key(self):
        self.store.save("key", "value")
        self.store.delete("key")
        self.assertEqual(self.store.key_exists("key"), False)