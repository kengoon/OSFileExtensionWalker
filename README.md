# OSFileExtensionWalker
This python module allows you to locate all specific file extension

example:

```python
from OSFEWalker.get_file_extension import get_file_extension
all_song = get_file_extension(r'.*\.mp3', music_folder)
```
the above example will return an iterator of all the mp3 files that exist in your Operating System
