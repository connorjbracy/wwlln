import sys

from backend.debug import  Debug

from script.utilities import ScriptParameterName, ScriptError

from wwlln.scripts.custom_logging import wwlln_logger


if (__name__ == '__main__'):
    globals__ = globals()

    try:
        storm   = globals__[ScriptParameterName.storm]
        success = storm.update_completeness()
        globals__[ScriptParameterName.success] = success

    except ScriptError as error:
        globals__[ScriptParameterName.success] = False
        globals__[ScriptParameterName.error]   = error
    except NameError as error:
        error = ScriptError('Undefined required variable "{}"'.format(error))
        globals__[ScriptParameterName.success] = False
        globals__[ScriptParameterName.error]   = error
    except:
        error_type    = sys.exc_info()[0]
        error_message = sys.exc_info()[1]
        wwlln_logger.error('Unpredicted Error({}): {}'.format(error_type, error_message))
        error = ScriptError('Unexpected Error({}): "{}"'.format(error_type,
                                                                error_message))
        globals__[ScriptParameterName.success] = False
        globals__[ScriptParameterName.error]   = error
