import datetime
import re
#import resource
from wwlln.scripts.file_io import create_path
from wwlln.scripts.url_request import request_list_dir
from TCDataCollection.models import Source, Resource
from TCDataProcessing.models import Storm, Mission, Sensor
from TCDataProcessing.models import Sensor
from TCDataProcessing.scripts.python.trackfile import TrackFile
from TCFrontEnd.models import Product
from wwlln.scripts.custom_logging import wwlln_logger


_REGIONS_OLD = [ 'ATL', 'CPAC', 'EPAC', 'IO', 'SHEM', 'WPAC']

_REGIONS_NEW = [ 'AL', 'CP','EP', 'IO', 'LS', 'SH','WP']

def find_navy_storms(region=None, season_num=None):
    wwlln_logger.info(str(locals()))
    stormsFound = []
    if(not isinstance(region,list)):
        region = [region]
    if(not isinstance(season_num,list)):
        season_num = [season_num]
    for r in region:
        for s in season_num:
            url = ('https://www.nrlmry.navy.mil/TC/tc{Season}/{Region}/'
                .format(Season = s, Region = r))
            list_dir = request_list_dir(url)
            if(list_dir):
                stormsFound += list_dir['dirs']
    return stormsFound


def find_new_storms(region=None, season_num=None,storm_num=None, date_range=None):
    wwlln_logger.info(str(locals()))
    if(region==None):
        region = _REGIONS_NEW
    if(not isinstance(region,list)):
        region = [region]
    if(season_num==None):
        season_num = datetime.datetime.now().year
    #old_storms = Storm.objects.all()
    old_storms = Storm.objects.all().filter(region = region, season_number = (season_num % 100), storm_number = storm_num)
    wwlln_logger.debug('\n'.join([f'old_storms[{i_storm}] = {old_storm}' for i_storm, old_storm in enumerate(old_storms)]))
    navy_storms = find_navy_storms(region, season_num if season_num>2000 else season_num+2000)
    wwlln_logger.debug(f'navy_storms (region={region}, season_num={season_num}, storm_num={storm_num}, date_range={date_range})\n{navy_storms}')
    storm_re = re.compile(r'[a-zA-z]{2}\d{6}')
    for storm in navy_storms:
        re_result = storm_re.search(storm) 
        if re_result:
            storm_result = re_result.group(0)
            storm_id = int(storm_result[2:4])
            wwlln_logger.debug(f'storm_result = {storm_result} | storm_id = {storm_id}')
            wwlln_logger.debug(f'if (not storm_num={storm_num} and storm_id={storm_id} <90) or storm_id({storm_id})==storm_num({storm_num}):')
            if (not storm_num and storm_id<90) or storm_id==storm_num:
                storm_region = storm_result[0:2]
                storm_season = int(storm_result[-2:])
                cur_storm = Storm(
                    storm_number = storm_id,
                    region = storm_region,
                    season_number = storm_season,
                    last_modified = datetime.datetime.min
                )
                wwlln_logger.debug(f'storm_result = {storm_result} | storm_id = {storm_id} | storm_region = {storm_region} | storm_season = {storm_season} | cur_storm = {cur_storm}')
                wwlln_logger.debug('if(not old_storms.filter(storm_number = cur_storm.storm_number({})).exists() = {}'.format(cur_storm.storm_number, (not old_storms.filter(storm_number = cur_storm.storm_number).exists())))
                if(not old_storms.filter(storm_number = cur_storm.storm_number).exists()):
                    wwlln_logger.debug(f'({cur_storm}).save()')
                    cur_storm.save()
        else:
            wwlln_logger.error('invalid listdir entry found: {} with attempted regex string: {}'.format(storm,r'[a-zA-z]{2}\d{6}'))
            #print('invalid listdir entry found: {} with attempted regex string: {}'.format(storm,r'[a-zA-z]{2}\d{6}'))

def update_storm_info(storm,dir):
    wwlln_logger.info(str(locals()))
    track = TrackFile()
    track.parseNavyTrackFile(create_path(dir,'trackfile.txt'))
    storm_name = track.get_storm_name()
    if storm_name:
        storm.name = storm_name.capitalize()
    storm.date_start = track.get_start_date()
    storm.date_end = track.get_end_date()
    storm.save()

def update_storm_resources(storms=None, resources=None):
    wwlln_logger.info(str(locals()))
    if not resources:
        resources = Resource.objects.all()
    elif not isinstance(resources,list):
        resources = [resources]
    if not storms:
        storms = Storm.objects.filter(is_complete=False)
    elif not isinstance(storms,list):
        storms = [storms]
    sensors = Sensor.objects.all()
    for resource in resources:
        for storm in storms:
            for sensor in sensors:
                dir = resource.collect(storm=storm,mission=sensor.mission,sensor=sensor,date_time=datetime.datetime.now())
                if resource.name == 'trackfile' and dir:
                    update_storm_info(storm,dir)

def update_storm_products(storms=None, products=None):
    wwlln_logger.info(str(locals()))
    if not products:
        products = Product.objects.all()
    elif not isinstance(products,list):
        products = [products]
    if not storms:
        storms = Storm.objects.filter(is_complete=False)
    elif not isinstance(storms,list):
        storms = [storms]
    
    
