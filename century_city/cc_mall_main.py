
import pandas as pd 
import os, sys 

'''
    find main LA dataframe on the hard disk,
    add it's path to the list of paths,
    import it 
'''

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\la_confidential\la_data'
sys.path.append(file_path)

from data import la_crime 

def get_2020_crime(lac:pd.DataFrame) -> pd.DataFrame:

    '''get dataframe for 2020'''
    
    la_2020 = lac[lac['Date Occurred'].str.contains('2020')]
    cc_mall_2020 = la_2020[la_2020['Location'] == '10200 SANTA MONICA BL']
    return cc_mall_2020

def get_2021_crime(lac:pd.DataFrame) -> pd.DataFrame:

    '''get dataframe for 2021'''
    
    la_2021 = lac[lac['Date Occurred'].str.contains('2021')]
    cc_mall_2021 = la_2021[la_2021['Location'] == '10200 SANTA MONICA BL']
    return cc_mall_2021

def get_2022_crime(lac:pd.DataFrame) -> pd.DataFrame:

    '''get dataframe for 2022'''
    
    la_2022 = lac[lac['Date Occurred'].str.contains('2022')]
    cc_mall_2022 = la_2022[la_2022['Location'] == '10200 SANTA MONICA BL']
    return cc_mall_2022

def get_2020_to_2022_crime(lac: pd.DataFrame) -> pd.DataFrame:

    '''get dataframe for 2020-2022'''

    la_2020_2022 = lac[
        (lac['Date Occurred'].str.contains('2020')) | 
        (lac['Date Occurred'].str.contains('2021')) | 
        (lac['Date Occurred'].str.contains('2022'))
        ]
    cc_mall_2020_2022 = la_2020_2022[la_2020_2022['Location'] == '10200 SANTA MONICA BL']
    return cc_mall_2020_2022

crime_2020 = get_2020_crime(la_crime)
crime_2021 = get_2021_crime(la_crime)
crime_2022 = get_2022_crime(la_crime)
crime_2020_2022 = get_2020_to_2022_crime(la_crime)
