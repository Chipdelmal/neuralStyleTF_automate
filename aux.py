import glob


def getFilesWithExt(path, ext=('*.png', '*.jpg', '*.jpeg')):
    filesList = []
    for files in ext:
        filesList.extend(glob.glob(path + files))
    return filesList
