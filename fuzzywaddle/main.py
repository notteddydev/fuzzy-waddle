"""Module with logic to copy and rename files provided in arguments into directories named after file type."""

import os
import os.path
import sys
import time

from pathlib import Path
from shutil import copy2, SameFileError
from curlywaffle.main import get_unique_file_path

PARENT_DESTINATION_DIR = f'{os.path.dirname(__file__)}/processed'

files_to_rename = sys.argv[1:]
file_count = len(files_to_rename)

if file_count == 0:
    print('Give me some files!')
    sys.exit()

print(f'Copying {file_count} file(s) and renaming them...')

failed_files = set()
for original_file_path in files_to_rename:
    file_extension = Path(original_file_path).suffix
    if not file_extension:
        failed_files.add(original_file_path)
        continue

    destination_dir = f'{PARENT_DESTINATION_DIR}/{file_extension[1:].lower()}'
    if not os.path.isdir(destination_dir):
        os.mkdir(destination_dir)

    modified_time_float = os.path.getmtime(original_file_path)
    modified_timestamp = time.ctime(modified_time_float)
    modified_datetime_object = time.strptime(modified_timestamp)
    modified_datetime_formatted = time.strftime("%Y-%m-%d %H.%M.%S", modified_datetime_object)
    
    proposed_file_path = f'{destination_dir}/{modified_datetime_formatted}{file_extension}'
    try:
        copy2(original_file_path, get_unique_file_path(proposed_file_path))

    except (PermissionError, SameFileError):
        failed_files.add(original_file_path)

failed_count = len(failed_files)
print(f'Successfully copied {file_count - failed_count} file(s).')
print(f'{failed_count} file(s) were unsuccessful.')

for file_to_rename in failed_files:
    print(f'{file_to_rename} failed to copy.')