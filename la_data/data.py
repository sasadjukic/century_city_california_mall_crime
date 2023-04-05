
import pandas as pd
from pathlib import Path 

main_directory = Path(__file__).parents[1]
data_file = main_directory / 'LA_Crime_Data_from_2020_to_Present.csv'

la_data = pd.read_csv(data_file)

def crime_sheet(la_data: pd.DataFrame) -> pd.DataFrame:

    crime_la = la_data
    return crime_la 

la_crime = crime_sheet(la_data)






