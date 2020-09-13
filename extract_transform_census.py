import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import numpy as np

# Block group level ACS data for Pennsylvania

state = '42' # Pennsylvania

# Counties list from reference file
counties = ['001','003','005','007','009','011','013','015','017','019','021','023','025','027','029','031','033',
            '035','037','039','041','043','045','047','049','051','053','055','057','059','061','063','065','067',
            '069','071','073','075','077','079','081','083','085','087','089','091','093','095','097','099','101',
            '103','105','107','109','111','113','115','117','119','121','123','125','127','129','131','133']

# List of selected features
features = "State,County,County_name,Block_Group,avg_Agg_HH_INC_ACS_14_18,avg_Agg_House_Value_ACS_14_18,avg_Tot_Prns_in_HHD_ACS_14_18,Crowd_Occp_U_ACS_14_18,ENG_VW_ACS_14_18,Female_No_HB_ACS_14_18,Females_ACS_14_18,Hispanic_ACS_14_18,LAND_AREA,Males_ACS_14_18,Med_HHD_Inc_BG_ACS_14_18,Median_Age_ACS_14_18,MrdCple_Fmly_HHD_ACS_14_18,NH_AIAN_alone_ACS_14_18,NonFamily_HHD_ACS_14_18,Not_HS_Grad_ACS_14_18"

# Write each county data to a separate csv file
for county in counties:
    r = requests.get(
        url="https://api.census.gov/data/2020/pdb/blockgroup?get={}&for=block%20group:*&in=state:{}%20county:{}".format(
            features, state, county))

    raw_data = eval(r.text.replace("null", '''"NA"'''))
    data = pd.DataFrame(raw_data[1:], columns=raw_data[0])
    data = data[features.split(',')]
    data['avg_Agg_HH_INC_ACS_14_18'] = data['avg_Agg_HH_INC_ACS_14_18'].transform(
        lambda x: np.NaN if x == 'NA' else int(re.sub('[^0-9]+', '', x)))
    data['avg_Agg_House_Value_ACS_14_18'] = data['avg_Agg_House_Value_ACS_14_18'].transform(
        lambda x: np.NaN if x == 'NA' else int(re.sub('[^0-9]+', '', x)))
    data['Med_HHD_Inc_BG_ACS_14_18'] = data['Med_HHD_Inc_BG_ACS_14_18'].transform(
        lambda x: np.NaN if x == 'NA' else int(re.sub('[^0-9]+', '', x)))
    data = data.replace('NA', np.NaN)
    data.to_csv("ACS_data_PA_{}.csv".format(county), index=False)

# Generate data description file

r = requests.get("https://api.census.gov/data/2020/pdb/blockgroup/variables.html")
soup = BeautifulSoup(r.text)

data = []
rows = soup.find('table').find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

data_description = pd.DataFrame(data[2:]).iloc[:,0:2]
data_description.columns = ['Name', "Description"]
data_description = data_description[data_description.Name.isin(features.split(','))]

data_description.to_csv("acs_data_description.csv", index=False)