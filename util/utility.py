"""Utility functions of the package music
"""

# This import does not work:
# from ..settings import settings

# However, this one (based on https://stackoverflow.com/questions/10272879/how-do-i-import-a-python-script-from-a-sibling-directory) does:
import sys
import os
sys.path.append(os.path.abspath('../settings'))
from settings import settings

from pathlib import Path


def get_project_dir():
    """Returns the Path object corresponding to the project root directory.
    """

    return Path(settings.PROJECT_DIR)


def get_data_dir():
    """Returns the Path object corresponding to the data directory
    (by convention located right under the project root directory).
    """

    data_dir = get_project_dir() / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


# if __name__ == '__main__':

#     # test pathlib.Path()
#     print()
#     # # current_dir = Path('.')                                             # print() and str() return only '.'
#     current_dir = Path('.').absolute()
#     print('Current dir:', current_dir)
#     print('Parent dir:', current_dir.parent)
#     new_dir = current_dir.parent / 'new'
#     print('new_dir:', new_dir)
#     # print('type(new_dir):', type(new_dir))
#     print('Path.cwd():', Path.cwd())
#     print('PROJECT_DIR:', settings.PROJECT_DIR)
#     print('get_project_dir():', get_project_dir())
#     print()
#     # new_dir = Path.cwd() / 'new/data/blues'
#     # new_dir.mkdir(parents=True, exist_ok=True)
#     # new_dir.rmdir()                                                     # rmdir() requires the dir to be empty
#     # print(new_dir)

#     print('get_data_dir():', get_data_dir())
#     # because_the_night = song.Song('Because the Night')
#     # file = get_data_dir() / 'because_the_night.txt'
#     # file.write_text(str(because_the_night))
#     # song = file.read_text()
#     # print(song)
#     #
#     # # print(Path.home())
#     # print()

#     # file = Path(settings.PROJECT_DIR) / 'data/Because the Night.txt'
#     # # print(file)
#     # lyrics = file.read_text()
#     # words = lyrics.split()
#     # # print(type(words))
#     # word_counter = Counter(words)
#     # most_common_10 = word_counter.most_common(10)
#     # least_common_10 = word_counter.most_common()[:-10-1:-1]             # n least common: [:-n-1:-1]
#     # print(most_common_10)
#     # print(least_common_10)
#     # print(sorted(least_common_10))
#     # print()



