
import matplotlib.pyplot as plt 
import os, sys 
import pandas as pd

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\la_confidential\century_city'
sys.path.append(file_path)

from cc_mall_2020_2022_crime import top_ten

def display_top_ten_cc_mall_crimes(cc_crimes: pd.Series) -> None:

    crimes = cc_crimes.index.tolist()
    values = cc_crimes.values.tolist()
    
    crimes.reverse()
    values.reverse()

    bg_color = '#292c2c'
    color = '#ffb4b4'
    highlight_color = '#fdf7c3'
    tick_color = '#5f4e4e'

    fig, ax = plt.subplots()

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.barh(
            crimes, 
            values, 
            color=color
        )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(tick_color)
    ax.spines['bottom'].set_color(tick_color)

    plt.xticks(color = tick_color)
    plt.yticks(color = highlight_color)

    for index, value in enumerate(values):
        plt.text(
            value, 
            index, 
            str(value),
            position = (value - 9, index - 0.125),
            color = bg_color,
            fontweight = 'bold',
            fontsize = 15
        )

    plt.show()

display_top_ten_cc_mall_crimes(top_ten)


