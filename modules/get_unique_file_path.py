"""Module for helper function which gets the unique file path to save a file to."""

import os


def get_unique_file_path(standard_file_path, file_extension):
    """Either returns the standard file path or modifies it with its duplicate number to ensure a unique file path."""
    if not os.path.isfile(f'{standard_file_path}{file_extension}'):
        return f'{standard_file_path}{file_extension}'

    checking_for_duplicates = True
    duplicate_count = 0

    while checking_for_duplicates:
        duplicate_count += 1
        checking_for_duplicates = os.path.isfile(
            f'{standard_file_path}-{duplicate_count}{file_extension}')

    return f'{standard_file_path}-{duplicate_count}{file_extension}'
