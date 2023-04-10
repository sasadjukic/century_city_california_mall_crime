
import matplotlib.pyplot as plt 
import os, sys 

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\la_confidential\century_city'
sys.path.append(file_path)

from cc_mall_assaults import a_assaults_2020, s_assaults_2020

def display_cc_mall_assaults_2020(a_2020: int, s_2020: int) -> None:

    aggravated = a_2020 
    simple = s_2020 

    colors = ['#FFB4B4', '#FDF7C3']
    fig = plt.subplots()

    plt.pie(
        [simple, aggravated],
        colors = colors,
        startangle = 25,
    )

    plt.show()

display_cc_mall_assaults_2020(a_assaults_2020, s_assaults_2020)
