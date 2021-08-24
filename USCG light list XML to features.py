## Pandas Read XML - https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.read_xml.html
## Light Lists: https://www.navcen.uscg.gov/?pageName=lightListWeeklyUpdates

import pandas
light_listD01 = pandas.read_xml('https://www.navcen.uscg.gov/pdf/lightLists/weeklyUpdates/v1d01WeeklyChanges.xml')
light_listD01