# Overview

FileStore is a simple key-value store that persists data to the file system.

# Examples

```
import file_store import FileStore

db = FileStore("/tmp")
db.save("foo", "bar")
assert db.get("foo") == "bar"

```