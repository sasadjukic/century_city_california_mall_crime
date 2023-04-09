
import pandas as pd
from cc_mall_help import la_crime_2020, la_crime_2021, la_crime_2022

# We already know top 10 crime spots from the la_metro_area package and top_crime_spots.py module
# Create a dictionary with top 10 crime spots in LA metro area to populate crime numbers from 2020-2022

top_crime_spots = {
       '800 N ALAMEDA ST' : {'2020' : 0, '2021' : 0, '2022' : 0},
       '10200 SANTA MONICA BL': {'2020' : 0, '2021' : 0, '2022' : 0},
       '100 THE GROVE DR': {'2020' : 0, '2021' : 0, '2022' : 0},
       '9300 TAMPA AV' : {'2020' : 0, '2021' : 0, '2022' : 0},
       '700 S FIGUEROA ST' : {'2020' : 0, '2021' : 0, '2022' : 0},
       '6600 TOPANGA CANYON BL' : {'2020' : 0, '2021' : 0, '2022' : 0},
       '700 W 7TH ST' : {'2020' : 0, '2021' : 0, '2022' : 0},
       '600 S SPRING ST' : {'2020' : 0, '2021' : 0, '2022' : 0},
       '600 S BROADWAY' : {'2020' : 0, '2021' : 0, '2022' : 0},
       '6800 HOLLYWOOD BL' : {'2020' : 0, '2021' : 0, '2022' : 0}
}

def populate_crimes_from_2020(tcs: dict[dict[str:int]], lac_2020: pd.DataFrame) -> dict[dict[str:int]]:

    '''update numbers for 2020'''

    for i in lac_2020.index:
        location = lac_2020.loc[i, 'Location']
        if location in tcs.keys():
            tcs[location]['2020'] += 1
    
    return tcs

def populate_crimes_from_2021(tcs: dict[dict[str:int]], lac_2021: pd.DataFrame) -> dict[dict[str:int]]:

    '''update numbers for 2021'''

    for i in lac_2021.index:
        location = lac_2021.loc[i, 'Location']
        if location in tcs.keys():
            tcs[location]['2021'] += 1
    
    return tcs

def populate_crimes_from_2022(tcs: dict[dict[str:int]], lac_2022: pd.DataFrame) -> dict[dict[str:int]]:

    '''update numbers for 2022'''

    for i in lac_2022.index:
        location = lac_2022.loc[i, 'Location']
        if location in tcs.keys():
            tcs[location]['2022'] += 1
    
    return tcs
        
pc_2020 = populate_crimes_from_2020(top_crime_spots, la_crime_2020)
pc_2021 = populate_crimes_from_2021(top_crime_spots, la_crime_2021)
pc_2022 = populate_crimes_from_2022(top_crime_spots, la_crime_2022)





