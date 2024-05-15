# Python script for organising files by file type and modification date.

Example resulting file paths:
```bash
/processed_files_dir/jpg/'2000-12-31 16.59.37.jpg'
/processed_files_dir/png/'2015-04-08 01.02.09.png'
```

### Requirements:
#### Software:
 - python3

### How to use:
```bash
cd /path/you/want/to/copy/files/to
python3 /path/to/fuzzy-waddle/main.py /path/to/file1 /path/to/file2 /path/to/file3
```

> [!NOTE]
> The 'processed_files_dir' directory if non-existent will be created in the directory that the python script is run from.