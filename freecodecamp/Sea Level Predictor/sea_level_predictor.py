import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='red', marker='+')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    year_extended = np.arange(df['Year'].min(), 2051)
    best_fit_line_1 = slope * year_extended + intercept
    plt.plot(year_extended, best_fit_line_1, color='blue') # , label='Best fit line #1'

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    best_fit_line_2 = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, best_fit_line_2, color='green') # , label='Best fit line #2'

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # plt.legend()


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()