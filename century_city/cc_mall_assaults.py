
import pandas as pd 
from cc_mall_main import crime_2020, crime_2021, crime_2022

'''store assault codes'''
aggravated_assaults = [230, 236]
simple_assaults = [624, 625, 626]

def get_cc_mall_2020_aggravated_assaults(cc_2020: pd.DataFrame) -> int:

    '''get aggrevated assaults for 2020'''
    
    agg_assaults = cc_2020[cc_2020['Crm Cd'].isin(aggravated_assaults)]
    return len(agg_assaults.index)

def get_cc_mall_2020_simple_assaults(cc_2020: pd.DataFrame) -> int:

    '''get simple and 'other' assaults for 2020'''

    sim_assaults = cc_2020[cc_2020['Crm Cd'].isin(simple_assaults)]
    return len(sim_assaults.index)

def get_cc_mall_2021_aggravated_assaults(cc_2021: pd.DataFrame) -> int:

    '''get aggrevated assaults for 2021'''

    agg_assaults = cc_2021[cc_2021['Crm Cd'].isin(aggravated_assaults)]
    return len(agg_assaults.index)

def get_cc_mall_2021_simple_assaults(cc_2021: pd.DataFrame) -> int:

    '''get simple and 'other' assaults for 2021'''

    sim_assaults = cc_2021[cc_2021['Crm Cd'].isin(simple_assaults)]
    return len(sim_assaults.index)

def get_cc_mall_2022_aggravated_assaults(cc_2022: pd.DataFrame) -> int:

    '''get aggrevated assaults for 2022'''

    agg_assaults = cc_2022[cc_2022['Crm Cd'].isin(aggravated_assaults)]
    return len(agg_assaults.index) 

def get_cc_mall_2022_simple_assaults(cc_2022: pd.DataFrame) -> int:

    '''get simple and 'other' assaults for 2022'''

    sim_assaults = cc_2022[cc_2022['Crm Cd'].isin(simple_assaults)]
    return len(sim_assaults.index)

a_assaults_2020 = get_cc_mall_2020_aggravated_assaults(crime_2020)
s_assaults_2020 = get_cc_mall_2020_simple_assaults(crime_2020)
a_assaults_2021 = get_cc_mall_2021_aggravated_assaults(crime_2021)
s_assaults_2021 = get_cc_mall_2021_simple_assaults(crime_2021)
a_assaults_2022 = get_cc_mall_2022_aggravated_assaults(crime_2022)
s_assaults_2022 = get_cc_mall_2022_simple_assaults(crime_2022)