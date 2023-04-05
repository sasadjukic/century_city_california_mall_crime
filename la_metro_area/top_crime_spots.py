
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

def find_places_with_most_crime(la: pd.DataFrame) -> dict[str:int]:
    
    '''makes a dictionary with locations and number of crimes commited'''

    crime_spot = {}

    for i in la.index:
        street = la.loc[i, 'Location']
        cross_street = la.loc[i, 'Cross Street']
        if type(cross_street) == float:
            location = street
        else: 
            location = str(street) + ' ' + str(cross_street)
        if location not in crime_spot:
            crime_spot[location] = 1
        else:
            crime_spot[location] += 1
    
    return crime_spot

def get_top_10_spots(sorted_crime: dict[str:int]) -> pd.Series:

    '''creates a panda Series of top 10 locations with most crimes'''

    top_10 = pd.Series(sorted_crime).nlargest(n=10)
    return top_10

def get_top_10_lat_and_long(t10: pd.Series, la: pd.DataFrame) -> dict[str:list]:

    '''will look for longitute and lattitude of the top crime spots for mapmaking'''
    locations = {}
    lat_lon = []
    top_10 = t10.index.tolist()

    for i in la.index:
        loc_name = la.loc[i, 'Location']
        lat = la.loc[i, 'LAT']
        lon = la.loc[i, 'LON']
        if loc_name in top_10 and loc_name not in locations:
            lat_lon.append(lat)
            lat_lon.append(lon)
            locations[loc_name] = lat_lon 
        else:
            lat_lon = []
    
    return locations

most_crime = find_places_with_most_crime(la_crime)
t_10 = get_top_10_spots(most_crime)
d10 = get_top_10_lat_and_long(t_10, la_crime)
print(t_10)
