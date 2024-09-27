import datetime
import logging
import logging.handlers

from wwlln.settings import BASE_DIR, SESSION_TYPE

LOG_BASE_DIR    = BASE_DIR.joinpath('logs')
SESSION_LOG_DIR = LOG_BASE_DIR.joinpath(SESSION_TYPE)
LOG_BASENAME    = ('wwlln_{}.log'.format(SESSION_TYPE))
LOG_FULLFILE    = SESSION_LOG_DIR.joinpath(LOG_BASENAME)

# Make sure the log directory eixsts
SESSION_LOG_DIR.mkdir(parents = True, exist_ok = True)

_formatter = logging.Formatter('{asctime} [{filename}({lineno}):{funcName}] {message}', style='{')

# TODO: Check what the SESSION_TYPE is when running the server as a live server
if ('server' in SESSION_TYPE.lower()):
  # TODO: Set to more reasonable backupcount
  num_sec_between_file_rotates = 5
  handler = TimedRotatingFileHandler(LOG_FULLFILE, 
                                     when        = 'midnight',
                                     interval    = num_sec_between_file_rotates,
                                     backupCount = 1000)
  # In case we are restarting a log session, rollover the previous log to make a clear distinction 
  # between sessions
  handler.doRollover()
else:
  # Matches the suffix generated for TimedRotatingFileHandler managed log files
  # TODO: Find a better way of programmatically copying the name
  log_file_timestamp_fmt    = logging.Formatter.default_time_format.replace(' ', '_').replace(':', '-')
  log_file_timestamp_suffix = datetime.datetime.now().strftime(log_file_timestamp_fmt)
  handler = logging.FileHandler('{}.{}'.format(LOG_FULLFILE, log_file_timestamp_suffix))

handler.setFormatter(_formatter)
wwlln_logger = logging.getLogger('wwlln_logger')
wwlln_logger.addHandler(handler)
# TODO: Set more meaningful log level (context dependent)
wwlln_logger.setLevel(logging.DEBUG)

# TODO: Review old doc/TODO and see if any of it needs to be supported at some point
#"""
#TODO
#
#-add custom flags eg: automation, data collection, display, etc
#-remove trailing log file text
#"""
#
#"""
#NONE         (-1) - Used to Disable Printing
#
#-VVV LEVELS USED BY PYTHON LOGGING VVV-
#ALL (NOTSET) ( 0) - Used to Print all messages
#DEBUG        (10) - Used to print messages to debug an application.
#INFO         (20) - Used to print general messages such as affirmations, confirmations, and success messages.
#WARNING      (30) - Used to report warnings, unexpected events due to inputs, indications for some problems that might arise in the future, etc.
#ERROR        (40) - Used to alert about serious problems that most probably will not stop the application from running.
#CRITICAL     (50) - Used to alert about critical issues that can harm the user data, expose the user data, hinder security, stop some service, or maybe end the application itself.
#"""


#"""
#Example call:
#
#from wwlln.scripts.custom_logging import _globalLogger
#
#_globalLogger.log_message("Requesting to view storm #{Storm}".format(Storm=storm), _globalLogger._DEBUG)
#"""
