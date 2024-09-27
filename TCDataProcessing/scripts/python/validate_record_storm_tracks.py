import os
import sys
import datetime

from django.utils import timezone

import backend.regex as regex
from backend.debug import Debug, DebugFunctionArgs
from script.utilities import ScriptError, ScriptParameterName
from storm.models import StormTrack

from wwlln.scripts.custom_logging import wwlln_logger


# Updates the track records for the given storm.
def validate_record_storm_tracks(storm, trackfile_filename):
    DebugFunctionArgs(print_to_stdout = False)
    if (not os.path.isfile(trackfile_filename)):
        wwlln_logger.error('Could not find trackfile: {}'.format(trackfile_filename))
        return False
    with open(trackfile_filename, 'rt') as track_records:
        wwlln_logger.info('Successfully opened the trackfile')
        # Extract each record of this storm from the track file.
        # [ 0] NNE -> N = zero padded storm number, E = extra ID character?
        # [ 1] Name
        # [ 2] Year
        # [ 3] Month
        # [ 4] Day
        # [ 5] Hour
        # [ 6] Minute
        # [ 7] Latitude
        # [ 8] N/S designation
        # [ 9] Longitude
        # [10] E/W designation
        # [11] Region name
        # [12] Wind Speed
        # [13] Pressure
        tracks = regex.find_all('(\d{2}.)\s+(\w+(?:-\w+)?)\s+(\d{2})(\d{2})(\d{2})\s+(\d{2})'
                                '(\d{2})\s+(\d+\.\d+)(\w)\s+(\d+\.\d+)(\w)\s+(\w+)\s+(\d+)\s+(\d+)',
                                track_records.read())
    wwlln_logger.info('Finished reading the trackfile')
    date_start   = timezone.now().date()
    date_end     = datetime.date(year = 1, month = 1, day = 1)
    storm_tracks = storm.stormtrack_set.all()
    # Loop through each track we found
    for track in tracks:
        wind_speed = int(track[12])
        pressure   = int(track[13])
        # Center the coordinates about the intersection of The Prime
        # Meridian and the Equator, with the northern and eastern
        # hemispheres being positive valued and the southern and western
        # hemispheres being negatively valued with respect to this
        # interseciton point.
        lat = float(track[7])
        lon = float(track[9])
        if (track[ 8] == 'S'):
            lat = -lat
        if (track[10] == 'W'):
            lon = -lon
        year = int(track[2])
        # If the century portion of the year is not there, add it.
        if (year < 2000):
            year += 2000
        # Extract the datetime info for the track record
        time = timezone.datetime(year   = year,
                                 month  = int(track[3]),
                                 day    = int(track[4]),
                                 hour   = int(track[5]),
                                 minute = int(track[6]))
        # Convert the timestamp to a timezone-aware datetime to please Django.
        time = timezone.make_aware(time)

        # Get the date of the track record
        track_record_date = time.date()
        # If this track record is more recent than the last known final
        # record for this storm, update that.
        if (date_end < track_record_date):
            date_end = track_record_date
        # Otherwise, check if the loaded track record predates the currently
        # known start date for the storm, and if it does update that.
        elif (date_start > track_record_date):
            date_start = track_record_date
        test_track = StormTrack(time       = time,
                                latitude   = lat,
                                longitude  = lon,
                                wind_speed = wind_speed,
                                pressure   = pressure)
        if (not storm_tracks.filter(time       = test_track.time,
                                    latitude   = test_track.latitude,
                                    longitude  = test_track.longitude,
                                    wind_speed = test_track.wind_speed,
                                    pressure   = test_track.pressure).exists()):
            wwlln_logger.info('Found a track in the trackfile that isn\'t in the database')
            raise ScriptError('For Storm "{Storm}", found track in file '
                              '"{File}" with data: '
                              'Time({Track.time}) | '
                              'Latitude({Track.latitude}) | '
                              'Longitude({Track.longitude}) | '
                              'WindSpeed({Track.wind_speed}) | '
                              'Pressure({Track.pressure}) '
                              'that did not have a corresponding entry in the '
                              'StormTrack database'
                              .format(Storm = storm, File = trackfile_filename, Track = test_track))
    wwlln_logger.info('All tracks in the trackfile were entered into the StormTrack database.')

    success = ((storm.date_start == date_start) and (storm.date_end == date_end))

    wwlln_logger.debug('Storm date range saved in Storm database: {} - {}\nStorm date range detected during testing: {} - {}\nFinal result of validation: {}'.format(storm.date_start, storm.date_end, date_start, date_end, success))

    return success


if (__name__ == '__main__'):
    globals__ = globals()

    try:
        wwlln_logger.info('Start {}'.format(__file__))
        #
        #storm     = globals__[ScriptParameterName.storm]
        #trackfile = globals__[ScriptParameterName.storm_trackfile]
        #
        #success = validate_record_storm_tracks(storm, trackfile)
        storm           = globals__[ScriptParameterName.storm]
        #input_dir       = globals__[ScriptParameterName.input_dir]
        #input_instances = globals__[ScriptParameterName.input_instances]
        input_instances_lists = globals__[ScriptParameterName.input_instances_lists]
        input_dir             = input_instances_lists[0].path
        input_instances       = input_instances_lists[0].files

        output_instances_list = globals__[ScriptParameterName.output_instances_list]
        output_dir            = output_instances_list.path
        output_instances      = output_instances_list.files

        wwlln_logger.debug('Loaded global parameters:\n{}\n{}\n'.format(storm, output_dir, input_instances))

        if (len(input_instances) > 1):
            raise ScriptError('Expected only 1 input file for recording Storm tracks, but we '
                              'receieved the following {} files: {}\n'
                              .format(len(input_instances), '\n'.join(input_instances)))

        success = validate_record_storm_tracks(storm, os.path.join(output_dir, input_instances[0]))
        wwlln_logger.info('Validated the script: {}'.format('Success' if success else 'Failure'))

        globals__[ScriptParameterName.success] = success
        wwlln_logger.info('Completed script, returning now...')

    except ScriptError as error:
        wwlln_logger.error('ScriptError: {}'.format(error))
        globals__[ScriptParameterName.success] = False
        globals__[ScriptParameterName.error]   = error
    except KeyError as error:
        wwlln_logger.error('KeyError: {}'.format(error))
        error = ScriptError('Undefined required GLOBAL variable "{}"'
                            .format(error))
        globals__[ScriptParameterName.success] = False
        globals__[ScriptParameterName.error]   = error
    except NameError as error:
        wwlln_logger.error('NameError: {}'.format(error))
        error = ScriptError('Undefined required LOCAL variable "{}"'.format(error))
        globals__[ScriptParameterName.success] = False
        globals__[ScriptParameterName.error]   = error
    except:
        error_type    = sys.exc_info()[0]
        error_message = sys.exc_info()[1]
        wwlln_logger.error('Unpredicted Error({}): {}'.format(error_type, error_message))
        error = ScriptError('Unexpected Error({}): "{}"'.format(error_type, error_message))
        globals__[ScriptParameterName.success] = False
        globals__[ScriptParameterName.error]   = error
