import pandas as pd

# platform locations
# https://www.data.boem.gov/Platform/Files/platlocfixed.zip
PL_filename = r"F:\LiveFeeds\BOEM\platloc.dat"
PL_fwidths = [3,8,3,2,6,15,6,1,6,1,17,17,14,13]
PL_colnames = ['DISTRICT_CODE', 'COMPLEX_ID_NUMBER', '	STRUCTURE_NUMBER', 'AREA_CODE', 'BLOCK_NUMBER', 'STRUCTURE_NAME',
            'SURFACE_NORTH_SOUTH_DISTANCE', 'NORTH_SOUTH_DEPARTURE_CODE', '	SURFACE_EAST_WEST_DISTANCE', 'EAST_WEST_DEPARTURE_CODE',
            'X_LOCATION', 'Y LOCATION', 'LONGITUDE', 'LATITUDE']

platform_locations = pd.read_fwf(PL_filename, widths = PL_fwidths, names = PL_colnames)
#print(platform_locations)

# platform master
# https://www.data.boem.gov/Platform/Files/platmastfixed.zip
PM_filename = r"F:\LiveFeeds\BOEM\platmast.dat"
PM_fwidths = [8,1,1,1,1,4,1,1,1,1,5,1,1,7,11,1,1,1,1,1,5,1,1,2,1,2,1,1,1,1,1,1,1,8,3,2,1,1,3,2,6,1]
PM_colnames = ['Complex Id Num', 'Abandon Flag', 'Aloc Mtr Flag', 'Attended 8 Hr Flag', 'Condn Prod Flag', 'Distance To Shore', 'Drilling Flag', 'Fired Vessel Fl',
               'Gas Prod Flag', 'Gas Flaring Flag', 'Mms Company Num', 'Manned 24 Hr Fl', 'Maj Cmplx Flag', 'Lease Number', 'Last Rev Date', 'Lact Mtr Flag','Injection Code',
               'Heliport Flag', 'Workover Flag', 'Water Prod Flag', 'Water Depth', 'Tank Gauge Flag', 'Sulfur Prod Flag', 'Subdistrict Code', 'Store Tank Flag', 'Rig Count',
               'Qtr Type', 'Prod Eqmt Flag', 'Production Flag', 'Power Source Type', 'Power Gen Flag', 'Oil Prod Flag', 'Gas Sale Mtr Flag', 'Field Name Code', 'District Code',
               'Crane Count', 'Compressor Flag', 'Comgl Prod Flag', 'Bed Count', 'Area Code', 'Block Number', 'Meter Prover Fl']

platform_master = pd.read_fwf(PM_filename, widths = PM_fwidths, names = PM_colnames)
#print(platform_master)

PLPM = platform_locations.merge(platform_master, left_on='COMPLEX_ID_NUMBER', right_on='Complex Id Num', how='left' )
#print(PLPM)

PLPM.to_csv(r"F:\LiveFeeds\BOEM\PLPM.csv")

# platform structures
# https://www.data.boem.gov/Platform/Files/platstrufixed.zip
PS_filename = r"F:\LiveFeeds\BOEM\platstru.DAT"
PS_fwidths = [2,6,8,2,1,11,11,1,1,11,3,3,3,3,15,3,5,6,6,3,16,8,20]
PS_colnames = ['Area Code', 'Block Number', 'Complex Id Num', 'Deck Count', 'East West Departure Code', 'Install Date', 'Last Revision Date', 'Major Structure Flag',
               'North South Departure Code', 'Removal Date', 'Slant Slot Count', 'Slot Count', 'Slot Drill Count', 'Satellite Completion Count', 'Structure Name',
               'Structure Number', 'Structure Type Code', 'Surface East West Distance', 'Surface North South Distance', 'Underwater Completion Count', 'Authority Type',
               'Authority Number', 'Authority Status']

platform_structures = pd.read_fwf(PS_filename, widths=PS_fwidths, names=PS_colnames)
#print(platform_structures)

PLPMPS = PLPM.merge(platform_structures, left_on='COMPLEX_ID_NUMBER', right_on='Complex Id Num', how='inner' )
#print(PLPMPS)

PLPMPS.to_csv(r"F:\LiveFeeds\BOEM\PLPMPS.csv")