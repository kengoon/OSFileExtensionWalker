import re
import os


def get_file_extension(regex, path):
    for folders, _, files in os.walk(path):
        if "." in folders or "Android" in folders:
            continue
        r = re.compile(regex)
        file_iterator = filter(r.match, files)
        for music_file in file_iterator:
            yield os.path.join(folders, music_file)
