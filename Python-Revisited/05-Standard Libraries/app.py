from pathlib import Path, PurePath, PureWindowsPath

# WORKING WITH FILE
# r is for raw string otherwise \ is considered as escape sequence
print(PureWindowsPath(r"E:\Work\Programming"))
print(PureWindowsPath(r"..\04-Modules"))
PureWindowsPath()                          # represent the current folder
print(PureWindowsPath())

# returns home directory of current user
# print(PureWindowsPath().home())
# print(PureWindowsPath().absolute())            # returns absolute path till parent folder

path = PurePath(r"..\04-Modules\ecommerce\__init__.py")

# print(path.exists())  # Check if given path exists or not
# print(path.is_file())  # Check if given path is a file
# print(path.is_dir())  # Check if given path is a dir
print(path.name)  # returns a file name
print(path.stem)  # returns a file name without extension
print(path.suffix)  # returns only extension of a file
print(path.parent)  # returns parent of path
# path = path.with_name("file.txt")       # change the file with same path
# print(path)

# change only extension of file with same path
path = path.with_suffix(".txt")
print(path)


# WORKING WITH DIRECTORIES

path = PurePath("ecommerce")
print(path)
# print(path.exists())
# path.mkdir()

# print(path.iterdir())
# for f in path.iterdir():
#     print(f)
