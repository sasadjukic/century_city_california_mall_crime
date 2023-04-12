
import matplotlib.pyplot as plt
import os, sys 

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\la_confidential\century_city'
sys.path.append(file_path)

from cc_mall_2020 import number_of_crimes_2020
from cc_mall_2021 import number_of_crimes_2021 
from cc_mall_2022 import number_of_crimes_2022

def display_rise_in_cc_mall_crimes(noc_2020: int, noc_2021: int, noc_2022: int) -> None:

    labels = ['2020', '2021', '2022']
    values = [noc_2020, noc_2021, noc_2022]

    bg_color = '#292c2c'
    color = '#ffb4b4'
    highlight_color = '#fdf7c3'
    tick_color = '#5f4e4e'

    fig, ax = plt.subplots()

    plt.plot(
        labels,
        values,
        marker='o',
        linestyle = 'solid',
        color = color
    )

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(tick_color)
    ax.spines['bottom'].set_color(tick_color)

    plt.suptitle(
        'CENTURY CITY MALL RISE IN CRIME',
        fontfamily = 'Russo One',
        fontsize = 18,
        color = color
    )

    plt.title(
        '*source https://catalog.data.gov/dataset/crime-data-from-2020-to-present',
        fontfamily = 'Russo One',
        color = tick_color
    )

    plt.ylabel(
        'NUMBER OF CRIMES',
        fontfamily = 'Russo One',
        fontsize = 12.5,
        color = tick_color
    )

    plt.xlabel(
        'YEAR',
        fontfamily = 'Russo One',
        fontsize = 12.5,
        color = tick_color
    )

    plt.xticks(color = highlight_color)
    plt.yticks(color = highlight_color)

    for index, value in enumerate(values):
        plt.text(
            index, 
            value, 
            str(value),
            position = (index - 0.055, value+5),
            color = highlight_color,
            fontweight = 'bold',
            fontsize = 15
        )

    plt.show()

display_rise_in_cc_mall_crimes(number_of_crimes_2020, number_of_crimes_2021, number_of_crimes_2022)