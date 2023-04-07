
import pandas as pd 
from cc_mall_main import crime_2020

def get_crimes_commited_cc_mall_2020(cc2020: pd.DataFrame) -> dict[str:int]:

    '''clasify crimes and count the numbers crimes had been commited in 2020'''

    crime_types = {}

    for i in cc2020.index:
        crime = cc2020.loc[i, 'Crm Cd Desc']
        if crime not in crime_types:
            crime_types[crime] = 1
        else:
            crime_types[crime] += 1

    return crime_types 

def top_five_commited_crimes_cc_mall_2020(crime_types: dict[str:int]) -> pd.Series:

    '''get top 5 most commited crimes for 2020'''

    return pd.Series(crime_types).nlargest(n=5)

number_of_crimes_2020 = len(crime_2020.index)
crime_types_2020 = get_crimes_commited_cc_mall_2020(crime_2020)
highest_ct_commited_2020 = top_five_commited_crimes_cc_mall_2020(crime_types_2020)