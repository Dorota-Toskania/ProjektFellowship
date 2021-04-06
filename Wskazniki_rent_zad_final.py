# -----------------------------------
# Downloading libraries
# -----------------------------------

import pandas as pd
import numpy as np
from numpy import inf

data_wsk = pd.read_csv('/Users/dorotagawronska-popa/PycharmProjects/ProjektFellowship/data/df_testy_as_columns.csv  ', index_col = 0)

def convert_period_to_year(period):
    year = period[-2:]
    if year[-1] == "*":
        year = period[-3:-1]
    if int(year) >= 10:
        year = "20" + str(year)
    else:
        print(period)
        year = "200" + str(year)
    # print(year)
    return year

# -----------------------------------
# Convert_period_to_year("Y 12.19")
# -----------------------------------

data_wsk["year"] = data_wsk["period"].map(convert_period_to_year)
data_wsk['Kapitał Stały'] = data_wsk['I. Kapitał własny'] + data_wsk['1. Zobowiązania długoterminowe']
data_wsk['Podatek'] = data_wsk['Zysk przed opodatkowaniem'] - data_wsk['V. Zysk netto']
data_wsk['Nopat'] = data_wsk['III. EBIT'] - data_wsk['Podatek']
    
print(data_wsk.columns)

# -----------------------------------
# Import wskaźniki zadłużenia od Martyny
# -----------------------------------

import wskazniki_zadluzenia

aktywa_ogol = data_wsk["Aktywa ogółem"].values
zob_ogol = data_wsk["II. Zobowiązania ogółem"].values
zob_dlug = data_wsk["1. Zobowiązania długoterminowe"].values
kapital_wlasny = data_wsk["I. Kapitał własny"].values
rsmt = data_wsk["2. Rzeczowe składniki majątku trwałego"].values

# -----------------------------------
# New columns vel wskazniki zadluzenia
# -----------------------------------

data_wsk["wog"] = wskazniki_zadluzenia.wog(zob_ogol, aktywa_ogol)
data_wsk["wzkw"] = wskazniki_zadluzenia.wzkw(zob_ogol, kapital_wlasny)
data_wsk["wdzo"] = wskazniki_zadluzenia.wdzo(zob_dlug, aktywa_ogol)
data_wsk["wdzkw"] = wskazniki_zadluzenia.wdzkw(zob_dlug, kapital_wlasny)
data_wsk["wuzd"] = wskazniki_zadluzenia.wuzd(zob_dlug, zob_ogol)
data_wsk["wpdr"] = wskazniki_zadluzenia.wpdr(rsmt, zob_dlug)

print(data_wsk)

wzkw = data_wsk["wzkw"].values
kapital_staly = data_wsk['Kapitał Stały'].values
data_wsk["wsk"] = wskazniki_zadluzenia.wsk(wzkw)
data_wsk["tsk"] = wskazniki_zadluzenia.tsk(kapital_staly, aktywa_ogol)

# -----------------------------------
# Rounding
# -----------------------------------

roa = round(data_wsk['V. Zysk netto']/data_wsk['Aktywa ogółem'], 6)*100
roe = round(data_wsk['V. Zysk netto']/data_wsk['I. Kapitał własny'], 6)*100
roic = round(data_wsk['Nopat']/data_wsk['Kapitał Stały'], 6)*100
ros = round(data_wsk['V. Zysk netto']/data_wsk['I. Przychody ze sprzedaży'], 6)*100
roce = round(data_wsk['III. EBIT']/data_wsk['Kapitał Stały'], 6)*100

data_wsk['wog'] = np.round(wskazniki_zadluzenia.wog(zob_ogol, aktywa_ogol), decimals=6)*100
data_wsk['wzkw'] = np.round(wskazniki_zadluzenia.wzkw(zob_ogol, kapital_wlasny), decimals=6)*100
data_wsk['wdzo'] = np.round(wskazniki_zadluzenia.wdzo(zob_dlug, aktywa_ogol), decimals=6)*100
data_wsk['wdzkw'] = np.round(wskazniki_zadluzenia.wdzkw(zob_dlug, kapital_wlasny), decimals=6)*100
data_wsk['wuzd'] = np.round(wskazniki_zadluzenia.wuzd(zob_dlug, zob_ogol), decimals=6)*100
data_wsk['wpdr'] = np.round(wskazniki_zadluzenia.wpdr(rsmt, zob_dlug), decimals=6)*100

data_wsk['wsk'] = np.round(wskazniki_zadluzenia.wsk(wzkw), decimals=6)*100
data_wsk["tsk"] = np.round(wskazniki_zadluzenia.tsk(kapital_staly, aktywa_ogol), decimals=6)*100

# -----------------------------------
# Infinity value
# -----------------------------------

def zamiana_inf(x):
    x[x==inf] = 0
    x[x==-inf] = 0
    return x

data_wsk['ROA'] = zamiana_inf(roa)
data_wsk['ROE'] = zamiana_inf(roe)
data_wsk['ROIC'] = zamiana_inf(roic)
data_wsk['ROS'] = zamiana_inf(ros)
data_wsk['ROCE'] = zamiana_inf(roce)
data_wsk['wog'] = zamiana_inf(data_wsk['wog'])
data_wsk['wzkw'] = zamiana_inf(data_wsk['wzkw'])
data_wsk['wdzo'] = zamiana_inf(data_wsk['wdzo'])
data_wsk['wdzkw'] = zamiana_inf(data_wsk['wdzkw'])
data_wsk['wuzd'] = zamiana_inf(data_wsk['wuzd'])
data_wsk['wpdr'] = zamiana_inf(data_wsk['wpdr'])
data_wsk['wsk'] = zamiana_inf(data_wsk['wsk'])
data_wsk['tsk'] = zamiana_inf(data_wsk['tsk'])

# print(data_wsk)

# -----------------------------------
# DataFrame with choosed indicators
# -----------------------------------

data_wsk = data_wsk[['ticker', 'year','ROA','ROE','ROIC','ROS','ROCE','wog','wzkw','wdzo','wdzkw','wuzd','wpdr','tsk','wsk']].sort_values(by='ticker')

# print(data_wsk)



