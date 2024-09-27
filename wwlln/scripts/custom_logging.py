import datetime
import logging
import logging.handlers
#from wwlln.settings import BASE_DIR
from os import chmod
import stat,sys

from wwlln.settings import BASE_DIR, SESSION_TYPE

#from logging.handlers import TimedRotatingFileHandler
LOG_BASE_DIR    = BASE_DIR.joinpath('logs')
SESSION_LOG_DIR = LOG_BASE_DIR.joinpath(SESSION_TYPE)
SESSION_LOG_DIR.mkdir(parents = True, exist_ok = True)
LOG_BASENAME    = ('wwlln_{}.log'.format(SESSION_TYPE))
LOG_FULLFILE    = SESSION_LOG_DIR.joinpath(LOG_BASENAME)

# format the log entries
#formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
#formatter = logging.Formatter('{asctime} {name} {levelname} {message}', style='{')
_formatter = logging.Formatter('{asctime} [{filename}::{funcName}:{lineno}] {message}', style='{')

# TODO: Check what the SESSION_TYPE is when running the server as a live server
if ('server' in SESSION_TYPE.lower()):
  # TODO: Set to more reasonable backupcount
  #test_log = './test.log'
  num_sec_between_file_rotates = 5
  #handler = TimedRotatingFileHandler(LOG_BASENAME, 
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
logger = logging.getLogger(__name__)
logger.addHandler(handler)
# TODO: Set more meaningful log level (context dependent)
logger.setLevel(logging.DEBUG)

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

class CustomLogger:
    _NONE     = -1
    _ALL      = logging.NOTSET
    _DEBUG    = logging.DEBUG
    _INFO     = logging.INFO
    _WARNING  = logging.WARNING
    _ERROR    = logging.ERROR
    _CRITICAL = logging.CRITICAL

    def __init__(self, _printLevel : int = _ALL, _printToConsole : bool = True, _printToFile : bool = True, _logFileName : str = "wwlln.log", _logTime : bool = True):
        self.printLevel : int = _printLevel
        self.printToConsole : bool = _printToConsole
        self.printToFile : bool = _printToFile
        self.logFilePath : str = str(BASE_DIR)+"/wwlln/logs/" + _logFileName
        self.logTime : bool = _logTime
        
        if self.printToFile:
            print("Logging To File/Console ENABLED")
            self.__logging_setup_file()
        elif self.printToConsole:
            print("Logging to Console ENABLED")
            self.__logging_setup_nofile()
        else:
            print("Warning: Logging DISABLED")
        
        self.log_message("BEGIN LOG", self._INFO)
    
    """
    Change rollover period to happen at midnight?
    """
    def __logging_setup_file(self):
        # set up logging to file
        logging.basicConfig(level=self.printLevel,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='[%d/%b/%Y %H:%M:%S]',
                    filename=self.logFilePath,
                    filemode='w')
        try:
            chmod(self.logFilePath, (stat.S_IREAD|stat.S_IWRITE|stat.S_IRGRP|stat.S_IWGRP|stat.S_IROTH))
        except PermissionError as e:
            print(e)
        handler = logging.handlers.TimedRotatingFileHandler(self.logFilePath, when='H', interval=1, backupCount=23)
        logging.getLogger('').addHandler(handler)

        if self.printToConsole:
            # define a Handler which writes [LEVEL] messages or higher to the sys.stderr
            console = logging.StreamHandler()
            console.setLevel(self.printLevel)
            # set a format which is simpler for console use
            formatter = logging.Formatter(fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='[%d/%b/%Y %H:%M:%S]',)
            # tell the handler to use this format
            console.setFormatter(formatter)
            # add the handler to the root logger
            logging.getLogger('').addHandler(console)
    
    def __logging_setup_nofile(self):
        logging.basicConfig(level=self.printLevel,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='[%d/%b/%Y %H:%M:%S]',)
    
    """
    special flags to be implimented later
    """
    def log_message(self, message : str, priorityLevel : int = _DEBUG, special=None):
        if self.printLevel < self._ALL or priorityLevel < self._NONE:
            return
        if priorityLevel == self._ALL:
            priorityLevel = self.DEBUG
        
        logging.log(priorityLevel, message)


_globalLogger = CustomLogger()

#"""
#Example call:
#
#from wwlln.scripts.custom_logging import _globalLogger
#
#_globalLogger.log_message("Requesting to view storm #{Storm}".format(Storm=storm), _globalLogger._DEBUG)
#"""
##import time
#
#import logging

#for handler in logger.handlers:
#    handler.doRollover()
#


#name – The name of the logger used to log the event represented by this LogRecord. Note that this name will always have this value, even though it may be emitted by a handler attached to a different (ancestor) logger.
#
#level – The numeric level of the logging event (one of DEBUG, INFO etc.) Note that this is converted to two attributes of the LogRecord: levelno for the numeric value and levelname for the corresponding level name.
#
#pathname – The full pathname of the source file where the logging call was made.
#
#lineno – The line number in the source file where the logging call was made.
#
#msg – The event description message, possibly a format string with placeholders for variable data.
#
#args – Variable data to merge into the msg argument to obtain the event description.
#
#exc_info – An exception tuple with the current exception information, or None if no exception information is available.
#
#func – The name of the function or method from which the logging call was invoked.
#
#sinfo – A text string representing stack information from the base of the stack in the current thread, up to the logging call.
#'################################################################################\nname = "{name}"\nlevel = "{level}"\npathname = "{pathname}"\nlineno = "{lineno}"\nmsg = "{msg}"\nargs = "{args}"\nexc_info = "{exc_info}"\nfunc = "{func}"\nsinfo = "{sinfo}"\n################################################################################'

