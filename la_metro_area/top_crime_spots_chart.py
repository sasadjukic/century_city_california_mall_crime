
import matplotlib.pyplot as plt 
import pandas as pd 
from top_crime_spots import t_10 

def display_top_10_crime_spots(t10: pd.Series) -> None:

    spots = t10.index.tolist()
    values = t10.values.tolist()

    values[:] = values[::-1]
    spots[:] = spots[::-1]

    temp_bar_color = '#ffb4b4'
    bg_color = '#292c2c'
    text_color = '#fdf7c3'
    text_color_sub = '#5f4e4e'

    fig, ax = plt.subplots()
    plt.barh(spots, values, color=temp_bar_color)

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(text_color_sub)
    ax.spines['bottom'].set_color(text_color_sub)

    plt.suptitle(
        'TOP 10 LOS ANGELES CRIME SPOTS SINCE 2020',
        fontfamily = 'Russo One',
        fontsize = 18,
        color = temp_bar_color
    )

    plt.title(
        '*source https://catalog.data.gov/dataset/crime-data-from-2020-to-present',
        fontfamily = 'Russo One',
        color = text_color_sub
    )

    plt.xlabel(
        'TOTAL CRIMES COMMITED',
        fontfamily = 'Russo One',
        fontsize = 12.5,
        color = text_color_sub
    )

    for index, value in enumerate(values):
        plt.text(
            value,
            index, 
            str(value),
            ha = 'center',
            position = (value-40, index-0.1),
            fontweight = 'bold',
            color = bg_color,
            fontsize = 15
        )

    plt.xticks(color=text_color_sub)
    plt.yticks(color=text_color)
    plt.show()

display_top_10_crime_spots(t_10)