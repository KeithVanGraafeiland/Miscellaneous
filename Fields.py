import pandas as pd

# all data comes from here: https://www.data.boem.gov/Main/FieldReserves.aspx

# Field Names Master Part One
# https://www.data.boem.gov/FieldReserves/Files/mastdatafixed.zip
FNM1_filename = r"F:\LiveFeeds\BOEM\appendafixed.txt"
FNM1_fwidths = [8,7,2,6,6,30,8,8,1,35]
FNM1_colnames = ['FIELD', 'LEASE', 'AREA', 'Block', 'EIA', 'DESIGNATED OPERATOR', 'EFF DATE', 'ETRC DATE', 'ETRC', 'PORTION OF LEASE WITHIN THE FIELD']

filename_master1 = pd.read_fwf(FNM1_filename, widths = FNM1_fwidths, names = FNM1_colnames)
print(filename_master1)

# Field Names Master Part Two
# https://www.data.boem.gov/FieldReserves/Files/mastprodfixed.zip
FNM2_filename = r"F:\LiveFeeds\BOEM\mastprodfixed.txt"
FNM2_fwidths = [8,7,16,16,16,16,16,16,16,8,]
FNM2_colnames = ['FIELD', 'LEASE', 'OIL(STB)', 'COND(STB)', 'Cumulative Oil', 'GAS(MCF)', 'CASINGHEAD GAS(MCF)', 'Cumulative Gas', 'WTR', '1STPROD']

filename_master2 = pd.read_fwf(FNM2_filename, widths = FNM2_fwidths, names = FNM2_colnames)
print(filename_master2)

# Appendix A - Area/Block to Field Index
# https://www.data.boem.gov/FieldReserves/Files/appendafixed.zip
AA_filename =r"F:\LiveFeeds\BOEM\appendafixed.txt"
AA_fwidths = [2,6,8,7,9]
AA_colnames = ['AREA', 'BLOCK', 'FIELD', 'LEASE', "AR_BLK"]

appendix_a = pd.read_fwf(AA_filename, widths = AA_fwidths, names = AA_colnames)
print(appendix_a)

FNM2AA = filename_master2.merge(appendix_a, on='FIELD', how='left' )
#print(FNM2AA)
FNM2AA.to_csv(r"F:\LiveFeeds\BOEM\FNM2AA.csv")