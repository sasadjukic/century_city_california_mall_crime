
'''
    1. This is a help module to track Century City mall rise in
    reported crimes in comparison to other locations in LA metro area
    2. To avoid complex time/space operations, first we split all commited la metro crimes 
    from 2020-2022 into a per year base
    3. This data will be exported to cc_mall_crime_growth_comparison.py
'''

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

def get_la_metro_crimes_for_2020(lac: pd.DataFrame) -> pd.DataFrame:

    '''get la metro area dataframe for 2020'''
    
    la_2020 = lac[lac['Date Occurred'].str.contains('2020')]
    return la_2020

def get_la_metro_crimes_for_2021(lac: pd.DataFrame) -> pd.DataFrame:

    '''get la metro area dataframe for 2021'''

    la_2021 = lac[lac['Date Occurred'].str.contains('2021')]
    return la_2021

def get_la_metro_crimes_for_2022(lac: pd.DataFrame) -> pd.DataFrame:

    '''get la metro area dataframe for 2021'''

    la_2022 = lac[lac['Date Occurred'].str.contains('2022')]
    return la_2022

la_crime_2020 = get_la_metro_crimes_for_2020(la_crime)
la_crime_2021 = get_la_metro_crimes_for_2021(la_crime)
la_crime_2022 = get_la_metro_crimes_for_2022(la_crime)