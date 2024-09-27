from os import symlink
import re
from pathlib import Path
from shutil import rmtree, copy
import shutil
from datetime import datetime, timezone

from wwlln.scripts.custom_logging import wwlln_logger


def create_file(filename,path='',is_text=False,Data=None, absolute=False):
  if not absolute:
    path = Path('.',path)
  file_mode = ('t' if is_text else 'b')
  full_path = Path(path,filename)
  #print('Writing to file "{}"...'.format(filename))
  wwlln_logger.info('Writing to file "{}"...'.format(full_path))
  wwlln_logger.debug('Contents:\n{}'.format(Data))
  if (Data):
    if (isinstance(Data, str)):
      file_mode = 't'
    elif (isinstance(Data, bytes)):
      file_mode = 'b'
    else:
      raise TypeError('Unknown type of Data to create file with: type(Data) = {}'.format(type(Data)))
    with full_path.open('w'+file_mode) as newFile:
      newFile.write(Data)

def copy_file(source_path,source_filename='',destination_path='',destination_filename='',absolute=False):
  if destination_path=='':
    destination_path=source_path
  if destination_filename=='':
    destination_filename=source_filename
  if not absolute:
    source_path = Path('.',source_path)
    destination_path = Path('.',destination_path)
  shutil.copy(Path(source_path,source_filename),Path(destination_path,destination_filename))

def delete_file(path, filename='', absolute=False):
  if not absolute:
    path = Path('.',path)
  to_delete = Path(path,filename)
  if to_delete.exists():
    to_delete.unlink()

def delete_files(path, filenames, absolute=False):
  if not absolute:
    path = Path('.',path)
  for filename in filenames:
    delete_file(path,filename)

def delete_directory(dirPath, absolute=False, force=False):
  if not absolute:
    dirPath = Path('.',dirPath)
  to_delete = Path(dirPath)
  link = Path(dirPath)
  try:
    if(to_delete.exists()):
      is_link = to_delete.is_symlink()
      if(is_link):
        to_delete = to_delete.readlink()
        link.unlink()
      if(force):
        rmtree(to_delete)
      elif(not is_link):
        to_delete.rmdir()
  except OSError:
    pass

def create_directory(dirPath, absolute=False, force=False):
  if not absolute:
    dirPath = Path('.',dirPath)
  to_create = Path(dirPath)
  delete_directory(dirPath,force)
  to_create.mkdir(parents=True,exist_ok=True)

def listdir(dirPath='', regex_pattern='.*', absolute=False):
  if not absolute:
    dirPath = Path('.',dirPath)
  result = []
  lastMod = []
  for dir in Path(dirPath).iterdir():
    if(re.match(regex_pattern,dir.name)):
      result.append(dir)
      lastMod.append(datetime.fromtimestamp(dir.stat().st_mtime))
  return {'dirs': result, 'last_modified': lastMod}

def create_path(*paths):
  return Path(*paths)

def get_last_modified_datetime(filename, path='', absolute=False):
  if not absolute:
    path = Path('.',path)
  file_path = Path(path,filename)
  if(file_path.exists()):
    return datetime.utcfromtimestamp(file_path.stat().st_mtime)
  return datetime.min

def get_parent(path, absolute=False):
  if not absolute:
    path = Path('.',path)
  if isinstance(path,Path):
    return path.parent
  return Path(path).parent

ROOT_PATH = create_path('/','wd3','storms','wwlln')
