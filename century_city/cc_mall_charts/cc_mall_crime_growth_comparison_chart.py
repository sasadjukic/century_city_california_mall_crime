
import matplotlib.pyplot as plt 
import os, sys 

userprofile = os.getenv('USERPROFILE')
file_path = f'{userprofile}\Desktop\github\la_confidential\century_city'
sys.path.append(file_path)

from cc_mall_crime_growth_comparison import pc_2022 

def display_cc_mall_crime_growth(lac: dict[dict[str:int]]) -> None:
    
    locations = [x for x in lac.keys()]
    values_2020 = [lac[i]['2020'] for i, v in lac.items()]
    values_2021 = [lac[i]['2021'] for i, v in lac.items()]
    values_2022 = [lac[i]['2022'] for i, v in lac.items()]
    years = [2020, 2021, 2022]

    colors = ['#fdf7c3', '#5f4e4e']
    text_color = '#ffb4b4'
    bg_color = '#292c2c'

    fig, ax = plt.subplots()

    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(colors[1])
    ax.spines['bottom'].set_color(colors[1])

    plt.xticks([2020, 2021, 2022], color=colors[0])
    plt.yticks(color=colors[0])

    plt.plot(years, [values_2020[0], values_2021[0], values_2022[0]], label=f'{locations[0]}', color=colors[1], linestyle='dotted')
    plt.plot(years, [values_2020[1], values_2021[1], values_2022[1]], label=f'{locations[1]}', color=colors[0], marker='o')
    plt.plot(years, [values_2020[2], values_2021[2], values_2022[2]], label=f'{locations[2]}', color=colors[1], linestyle='dotted')
    plt.plot(years, [values_2020[3], values_2021[3], values_2022[3]], label=f'{locations[3]}', color=colors[1], linestyle='dotted')
    plt.plot(years, [values_2020[4], values_2021[4], values_2022[4]], label=f'{locations[4]}', color=colors[1], linestyle='dotted')
    plt.plot(years, [values_2020[5], values_2021[5], values_2022[5]], label=f'{locations[5]}', color=colors[1], linestyle='dotted')
    plt.plot(years, [values_2020[6], values_2021[6], values_2022[6]], label=f'{locations[6]}', color=colors[1], linestyle='dotted')
    plt.plot(years, [values_2020[7], values_2021[7], values_2022[7]], label=f'{locations[7]}', color=colors[1], linestyle='dotted')
    plt.plot(years, [values_2020[8], values_2021[8], values_2022[8]], label=f'{locations[8]}', color=colors[1], linestyle='dotted')
    plt.plot(years, [values_2020[9], values_2021[9], values_2022[9]], label=f'{locations[9]}', color=colors[1], linestyle='dotted')

    plt.suptitle(
        'CENTURY CITY MALL CRIME GROWTH AMONG TOP 10 LA METRO AREA CRIME SPOTS',
        fontfamily = 'Russo One',
        fontsize = 18,
        color = text_color
    )

    plt.title(
        '*source https://catalog.data.gov/dataset/crime-data-from-2020-to-present',
        fontfamily = 'Russo One',
        color = colors[1]
    )

    plt.ylabel(
        'NUMBER OF CRIMES',
        fontfamily = 'Russo One',
        fontsize = 12.5,
        color = colors[1]
    )

    plt.xlabel(
        'YEAR',
        fontfamily = 'Russo One',
        fontsize = 12.5,
        color = colors[1]
    )

    plt.legend(framealpha=0, facecolor=bg_color)
    plt.show()

display_cc_mall_crime_growth(pc_2022)