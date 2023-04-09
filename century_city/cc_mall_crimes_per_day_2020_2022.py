

from cc_mall_2020 import number_of_crimes_2020
from cc_mall_2021 import number_of_crimes_2021
from cc_mall_2022 import number_of_crimes_2022

def get_crimes_per_day_2020(noc_2020: int) -> float:

    return round(noc_2020 / 366, 2) 

def get_crimes_per_day_2021(noc_2021: int) -> float:

    return round(noc_2021 / 365, 2)

def get_crimes_per_day_2022(noc_2022: int) -> float:

    return round(noc_2022 / 365, 2)

year_2020 = get_crimes_per_day_2020(number_of_crimes_2020)
year_2021 = get_crimes_per_day_2021(number_of_crimes_2021)
year_2022 = get_crimes_per_day_2022(number_of_crimes_2022)