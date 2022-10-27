"""Project configuration settings
"""


import os
from pathlib import Path


PROJECT_DIR = Path('.').absolute()

# # Alternative 1:
# PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))            # project root directory (str)

# # Alternative 2:
# PROJECT_DIR = os.path.abspath('')
# print(PROJECT_DIR)
# PROJECT_DIR = os.path.dirname(PROJECT_DIR)
# print(PROJECT_DIR)

# # Alternative 3:
# current_dir = Path('.').absolute()
# PROJECT_DIR = current_dir.parent
# print(current_dir)
# print(PROJECT_DIR)
