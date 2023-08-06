# DirDog

Simplest Watchdog for a given directory. Allows to register callbacks for newly created, deleted, or modified files. 

## Usage

```python
from dirdog import DirDog


def new_file_callback(file_name):
    print(file_name + " created!")


path_of_directory_to_monitor = "."
d = DirDog(path_of_directory_to_monitor)
d.on_new_file(new_file_callback)
d.join()

```