
import pandas as pd 
from cc_mall_main import crime_2020_2022

def get_crimes_commited_2020_2022(cc_crime: pd.DataFrame) -> dict[str:int]:

    '''get all crimes in CC mall from 2020-2022'''
    
    all_crime = {}

    for i in cc_crime.index:
        crime = cc_crime.loc[i, 'Crm Cd Desc']
        if crime not in all_crime:
            all_crime[crime] = 1
        else:
            all_crime[crime] += 1

    return all_crime 

def get_top_ten_crimes(all_crime: dict[str:int]) -> pd.Series:

    '''get top 10 crimes commited in CC mall from 2020-2022'''

    return pd.Series(all_crime).nlargest(n=10)

all_crimes = get_crimes_commited_2020_2022(crime_2020_2022)
top_ten = get_top_ten_crimes(all_crimes)