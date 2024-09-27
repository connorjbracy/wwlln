from django.db import models
from django.db.models.deletion import CASCADE
import wwlln.scripts.file_io as file_io
import wwlln.scripts.url_request as url_request
from wwlln.scripts.custom_logging import wwlln_logger
import re
import urllib.error
import datetime

# Create your models here.
class Source(models.Model):
  name = models.CharField(max_length=32)
  url_path = models.TextField()
  username = models.CharField(max_length = 64, null = True, default = None)
  password = models.CharField(max_length = 64, null = True, default = None)
  description = models.TextField()
  is_local = models.BooleanField()

  def __str__(self):
    return ('{Source.name}: {Source.description}'.format(Source = self))

class Resource(models.Model):
  source = models.ForeignKey(Source, on_delete=CASCADE)
  name = models.CharField(max_length=32)
  path = models.TextField()
  filename = models.TextField()
  description = models.TextField()
  local_path = models.TextField()

  def __str__(self):
    return ('{Resource.name}: {Resource.description}'.format(Resource = self))

  def collect(self, storm='', mission='', sensor='', date_time=None, force=False):
    try:
      is_local = self.source.is_local
      full_remote = None
      if is_local:
        full_remote = file_io.create_path(self.source.url_path, self.path)
      else:
       full_remote = url_request.createURL(self.source.url_path,self.path)
      
      if not date_time:
        date_time = datetime.datetime.now()

      formatted_remote = full_remote.format(Storm=storm, Mission=mission, Sensor=sensor, Year=date_time.year, Month=date_time.month, Day=date_time.day)
      formatted_path = self.local_path.format(Storm=storm, Mission=mission, Sensor=sensor, Year=date_time.year, Month=date_time.month, Day=date_time.day)
      formatted_filename = self.filename.format(Storm=storm, Mission=mission, Sensor=sensor, Year=date_time.year, Month=date_time.month, Day=date_time.day)
      filename_pat = re.compile(formatted_filename)
      wwlln_logger.debug('is_local           = {}'.format(is_local))
      wwlln_logger.debug('full_remote        = {}'.format(full_remote))
      wwlln_logger.debug('formatted_remote   = {}'.format(formatted_remote))
      wwlln_logger.debug('formatted_path     = {}'.format(formatted_path))
      wwlln_logger.debug('formatted_filename = {}'.format(formatted_filename))
      wwlln_logger.debug('filename_pat       = {}'.format(filename_pat))
      
      list_dir = None
      if is_local:
        list_dir = file_io.listdir(formatted_remote)
      else:
        list_dir = url_request.request_list_dir(formatted_remote,
                                                self.source.username,
                                                self.source.password)
      wwlln_logger.debug('list_dir = {}'.format(list_dir))
      if list_dir:
        resource_list = list_dir['dirs']
        last_modified = list_dir['last_modified']
        file_results=[]
                       
        for i in range(len(resource_list)):
          wwlln_logger.info('Processing resource list #{} of {}'.format(i, len(resource_list)))
          if re.match(filename_pat,str(resource_list[i])):
            file_results.append({'file':resource_list[i],'last_modified':last_modified[i]})
        
        for file in file_results:
          wwlln_logger.debug('File: "{}"'.format(file))
          wwlln_logger.debug('(local) Last Modified: "{}"'.format(file_io.get_last_modified_datetime(file['file'],formatted_path)))
          if file['last_modified']>file_io.get_last_modified_datetime(file['file'],formatted_path):
            if is_local:
              file_io.copy_file(file['file'],destination_path=formatted_path)
            else:
              file_url = url_request.createURL(formatted_remote,file['file'])
              file_data = url_request.request_url_contents(file_url,
                                                           self.source.username,
                                                           self.source.password)
              file_io.create_directory(formatted_path)
              file_io.create_file(file['file'],formatted_path,Data=file_data)
              wwlln_logger.info('successfully retrieved {filename}. new file located at {path}'.format(filename = file['file'],path = formatted_path))
              #wwlln_logger.info('successfully retrieved {filename}. new file located at {path}'
              #    .format(filename = file['file'],path = formatted_path))
      return file_io.create_path(formatted_path)
    except urllib.error.URLError as e:
      wwlln_logger.critical('URLError Occured: {}'.format(e))
      return False
    except OSError as e:
      wwlln_logger.critical('OSError Occured: {}'.format(e))
      return False
