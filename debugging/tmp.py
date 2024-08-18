import pathlib
import urllib.parse
import wwlln.scripts.url_request as url_request

navy_root       = 'https://www.nrlmry.navy.mil/TC/'
local_root_rel  = './test_data_root'
local_root_abs  = pathlib.Path(local_root_rel).absolute()

season_subdir   = 'tc20'
region_subdir   = 'ATL'
storm_subdir    = '01L.ARTHUR'
storm_rel_parts = [season_subdir, region_subdir, storm_subdir]

trackfile_filename       = 'trackfile.txt'
trackfile_path_rel_parts = (storm_rel_parts + [trackfile_filename])
trackfile_navy_path      = urllib.parse.urljoin(navy_root, trackfile_path_rel_parts)
#trackfile_path_rel = pathlib.Path(storm_subdirs[0]).joinpath(*(storm_subdirs[1:]), 
#                                                             trackfile_filename)
#trackfile_path_navy =  
#
#img_filename = '20200513.1016.f16.x.pct.90LINVEST.25kts-1011mb-242N-807W.057pc.jpg'
#img_path_rel = pathlib.Path(storm_subdirs[0]).joinpath(*(storm_subdirs[1:]), 
#                                                             img_filename)
#
#
#url_navy_home =
#url_navy_dir = 'https://www.nrlmry.navy.mil/TC/tc20/ATL/01L.ARTHUR/'
#url_navy_txt = 'https://www.nrlmry.navy.mil/TC/tc20/ATL/01L.ARTHUR/trackfile.txt'
#url_navy_img = 'https://www.nrlmry.navy.mil/TC/tc20/ATL/01L.ARTHUR/tc_ssmis/pct/20200513.1016.f16.x.pct.90LINVEST.25kts-1011mb-242N-807W.057pc.jpg'
#url_navy_404 = 'https://www.nrlmry.navy.mil/TC/badaddress'
#urls = [url_navy_home, url_navy_dir, url_navy_txt, url_navy_img, url_navy_404]
#pages = {}
#for url in urls:
#    try:
#        pages[url] = url_request.request_url_contents(url)
#    except ConnectionError as e:
#        print(e)
#url = urls[0]
#links = url_request.request_url_links(url)
#
