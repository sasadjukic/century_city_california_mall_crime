

import matplotlib.pyplot as plt 
import os, sys 

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\la_confidential\century_city'
sys.path.append(file_path)

from cc_mall_assaults import a_assaults_2022, s_assaults_2022

def display_cc_mall_assaults_2022(a_2022: int, s_2022: int) -> None:

    aggravated = a_2022 
    simple = s_2022 
    colors = ['#FFB4B4', '#FDF7C3']

    fig = plt.subplots()

    plt.pie(
        [simple, aggravated],
        colors = colors,
        startangle = 15,
    )

    plt.show()

display_cc_mall_assaults_2022(a_assaults_2022, s_assaults_2022)