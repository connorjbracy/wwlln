% Make sure MATLAB knows where out main scripts folder is
path(path, '/wd3/storms/wwlln/script/matlab');
set(0, 'DefaultFigureVisible', 'off');

storm__ = 0;
storm_name__ = 'Irma';
mission_sensor_map__ = containers.Map({'SSMIS', 'TRMM', 'SSMI', 'GPM'}, {{'F16', 'F17', 'F18', 'F19', 'F20'}, {'TMI'}, {'F10', 'F11', 'F12', 'F13', 'F14', 'F15'}, {'GMI'}});
resources__ = {0, 0, 0};
pipeline__ = 0;
product__ = 0;
product_name__ = 'GPM_DPR_Plot.';
input_instances_lists__ = {containers.Map({'path', 'files'}, {'/wd3/storms/wwlln/data/raw_data/17/ATL/11/', {'ATL_17_11_Irma_Reduced_Trackfile.txt', 'ATL_17_11_Irma_WWLLN_Locations.txt'}}), containers.Map({'path', 'files'}, {'/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2020/07/08/1C/GPM/GMI', 0}), containers.Map({'path', 'files'}, {'/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2020/07/08/radar/GPM/GMI', 0})};
output_instances_list__ = containers.Map({'path', 'files'}, {'/wd3/storms/wwlln/data/processed_data/17/ATL/11/dpr_plot', {'ATL_17_11_Irma_GMI_DPR_Plot_20170829T051100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170829T163600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170831T162600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170901T054600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170902T161600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170903T053600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170903T170100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170904T061600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170904T160600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170905T052600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170905T165100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170906T060600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170907T163600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170907T164100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170908T055600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170909T064100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170909T162600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170910T054600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170911T063100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170911T161600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170829T051100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170829T163600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170831T162600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170901T054600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170902T161600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170903T053600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170903T170100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170904T061600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170904T160600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170905T052600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170905T165100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170906T060600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170907T163600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170907T164100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170908T055600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170909T064100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170909T162600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170910T054600.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170911T063100.gif', 'ATL_17_11_Irma_GMI_DPR_Plot_20170911T161600.gif'}});
success__ = true;
storm_trackfile__ = '/wd3/storms/wwlln/data/raw_data/17/ATL/11/ATL_17_11_Irma_Reduced_Trackfile.txt';
storm_wwlln_locations__ = '/wd3/storms/wwlln/data/raw_data/17/ATL/11/ATL_17_11_Irma_WWLLN_Locations.txt';
wwlln_data_path__ = '/wd3/storms/wwlln/lightning';
storm_filename_prefix__ = 'ATL_17_11_Irma_';
date_time__ = datetime(2020, 07, 08, 14, 55, 57);
script__ = 0;
passtimes__ = {datetime(2017, 08, 29, 05, 11, 00), datetime(2017, 08, 29, 16, 36, 00), datetime(2017, 08, 31, 05, 01, 00), datetime(2017, 08, 31, 16, 26, 00), datetime(2017, 09, 01, 05, 46, 00), datetime(2017, 09, 02, 16, 16, 00), datetime(2017, 09, 03, 05, 36, 00), datetime(2017, 09, 03, 17, 01, 00), datetime(2017, 09, 04, 06, 16, 00), datetime(2017, 09, 04, 16, 06, 00), datetime(2017, 09, 05, 05, 26, 00), datetime(2017, 09, 05, 16, 51, 00), datetime(2017, 09, 06, 06, 06, 00), datetime(2017, 09, 07, 16, 36, 00), datetime(2017, 09, 07, 16, 41, 00), datetime(2017, 09, 08, 05, 56, 00), datetime(2017, 09, 09, 06, 41, 00), datetime(2017, 09, 09, 16, 26, 00), datetime(2017, 09, 10, 05, 46, 00), datetime(2017, 09, 11, 06, 31, 00), datetime(2017, 09, 11, 16, 16, 00), datetime(2017, 09, 12, 15, 21, 00), datetime(2017, 09, 13, 06, 21, 00)};
storm_coords__ = {{14.1, -22.4}, {15.5, -25.3}, {16.4, -32.5}, {17.1, -34.3}, {17.9, -36.1}, {18.7, -44.1}, {18.2, -46.7}, {17.7, -49.2}, {17.0, -51.7}, {16.7, -53.9}, {16.6, -56.4}, {16.9, -59.2}, {17.7, -61.9}, {20.7, -70.4}, {20.7, -70.4}, {21.5, -73.2}, {22.3, -78.3}, {23.1, -80.2}, {23.7, -81.3}, {28.2, -82.2}, {30.9, -83.5}, {30.9, -83.5}, {30.9, -83.5}};
raw_data_1C_files__ = {'/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/08/29/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170829-S044709-E061941.019891.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/08/29/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170829-S153458-E170730.019898.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/08/31/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170831-S043631-E060905.019922.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/08/31/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170831-S152440-E165715.019929.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/01/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170901-S051800-E065035.019938.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/02/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170902-S151502-E164736.019960.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/03/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170903-S050821-E064055.019969.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/03/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170903-S155629-E172904.019976.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/04/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170904-S054948-E072223.019985.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/04/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170904-S150521-E163755.019991.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/05/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170905-S045839-E063114.020000.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/05/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170905-S154647-E171921.020007.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/06/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170906-S054005-E071239.020016.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/07/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170907-S153700-E170934.020038.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/07/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170907-S153700-E170934.020038.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/08/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170908-S053017-E070251.020047.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/09/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170909-S061138-E074413.020063.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/09/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170909-S152709-E165942.020069.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/10/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170910-S052023-E065258.020078.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/11/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170911-S060143-E073417.020094.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/11/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170911-S151712-E164946.020100.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/12/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170912-S142555-E155829.020115.V05A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/13/1C/GPM/GMI/1C.GPM.GMI.XCAL2016-C.20170913-S055144-E072418.020125.V05A.HDF5'};
raw_data_2A_files__ = {'/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/08/29/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170829-S044709-E061941.019891.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/08/29/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170829-S153458-E170730.019898.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/08/31/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170831-S043631-E060905.019922.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/08/31/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170831-S152440-E165715.019929.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/01/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170901-S051800-E065035.019938.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/02/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170902-S151502-E164736.019960.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/03/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170903-S050821-E064055.019969.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/03/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170903-S155629-E172904.019976.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/04/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170904-S054948-E072223.019985.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/04/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170904-S150521-E163755.019991.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/05/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170905-S045839-E063114.020000.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/05/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170905-S154647-E171921.020007.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/06/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170906-S054005-E071239.020016.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/07/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170907-S153700-E170934.020038.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/07/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170907-S153700-E170934.020038.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/08/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170908-S053017-E070251.020047.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/09/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170909-S061138-E074413.020063.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/09/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170909-S152709-E165942.020069.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/10/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170910-S052023-E065258.020078.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/11/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170911-S060143-E073417.020094.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/11/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170911-S151712-E164946.020100.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/12/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170912-S142555-E155829.020115.V06A.HDF5', '/wd3/storms/wwlln/data/raw_data/shared/gpmdata/2017/09/13/radar/GPM/GMI/2A.GPM.DPR.V8-20180723.20170913-S055144-E072418.020125.V06A.HDF5'};