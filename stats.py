__author__ = "Javier Carracedo (@JaviKarra94)"
__copyright__ = "Copyright (c) 2022 Javier Carracedo"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Javier Carracedo"
__twiter__ = "@JaviKarra94"
__status__ = "Production"

import pandas as pd
import os
import matplotlib.pyplot as plt

def GenerateClassificationPNGFigures(urls, leagues):

    """Generates a set of images about raking points by each set of leagues.

    Parameters
    ----------
    urls : list
        List of urls with information about the leagues ranking.
    leagues : list
        Name of the leagues.

    """

    if not os.path.exists('Classification'):
        os.makedirs('Classification')

    for item in range(0, len(urls)):

        dfs = pd.read_html(urls[item])
        clasificacion = dfs[0]
        plot = clasificacion.plot(x="Squad", y=["Pts"], kind="bar", xlabel ="Teams", ylabel = "Points")
        fig = plot.get_figure()
        fig.savefig(os.path.join('.\Classification', leagues[item].strip()), bbox_inches='tight')

def GenerateFullClassificationPNGFigures(urls, leagues, rows, columns):

    """Generates an image with subplots of images about raking points by each set of leagues.

    Parameters
    ----------
    urls : list
        List of urls with information about the leagues ranking.
    leagues : list
        Name of the leagues.
    rows : list
        Number of rows in the plot.
    columns : list
        Number of columns in the plot.
    """

    if not os.path.exists('Classification'):
        os.makedirs('Classification')

    figure_full, axs = plt.subplots(nrows = rows, ncols = columns, figsize=(15, 10))
    figure_full.suptitle('Classification (Twitter: @JaviKarra94)')
    
    dataframes = []
    plots = []

    for item in range(0, len(urls)):        
        dfs = pd.read_html(urls[item])
        dataframes.append(dfs[0]) # Get clasificacion table league dataframe

    # Create plots
    for i in range(0, rows):
        for j in range(0, columns):
            plots.append(dataframes[j * rows + i].plot(x="Squad", y=["Pts"], kind="bar", ax=axs[i,j], title = leagues[j * rows + i], xlabel = "Teams", ylabel = "Points"))        

    for item in (range(0, len(plots))):
        plots[item].grid(axis='y', linestyle='--')

    figure_full.tight_layout()
    figure_full.savefig(os.path.join('.\Classification', 'AllLeagues'), bbox_inches='tight')

def GenerateFullGoalsForVsGoalsAgaintstPNGFigures(urls, leagues, rows, columns):

    """Generates an image with subplots of images about local goals vs against goals set of leagues.

    Parameters
    ----------
    urls : list
        List of urls with information about the leagues ranking.
    leagues : list
        Name of the leagues.
    rows : list
        Number of rows in the plot.
    columns : list
        Number of columns in the plot.
    """

    if not os.path.exists('Goals'):
        os.makedirs('Goals')

    figure_full, axs = plt.subplots(nrows=rows, ncols=columns, figsize=(15, 10))
    figure_full.suptitle('Goals For (GF) Vs Goals Againtst (GA) (Twitter: @JaviKarra94)')

    dataframes = []
    plots = []

    for item in range(0, len(urls)):
        dfs = pd.read_html(urls[item])
        dataframes.append(dfs[0]) # Get clasificacion table league dataframe

    # Create plots
    for i in range(0, rows):
        for j in range(0, columns):
            plots.append(dataframes[j * rows + i].plot(x="Squad", y=["GF","GA"], kind="bar", ax=axs[i,j], title = leagues[j * rows + i], xlabel = "Teams", ylabel = "Goals"))

    for item in (range(0, len(plots))):
        plots[item].grid(axis='y', linestyle='--')

    figure_full.tight_layout()
    figure_full.savefig(os.path.join('.\Goals', 'AllLeagues'), bbox_inches='tight')

def GenerateGoalsForVsGoalsAgaintstPNGFigures(urls, leagues):

    """Generates a set of images about local goals vs against goals set of leagues.

    Parameters
    ----------
    urls : list
        List of urls with information about the leagues ranking.
    leagues : list
        Name of the leagues.

    """

    if not os.path.exists('Goals'):
            os.makedirs('Goals')

    for item in range(0, len(urls)):

        dfs = pd.read_html(urls[item])
        clasificacion = dfs[0]
        plot = clasificacion.plot(x="Squad", y=["GF","GA"], kind="bar", xlabel ="Teams", ylabel = "Goals")
        fig = plot.get_figure()
        fig.savefig(os.path.join('.\Goals', leagues[item].strip()), bbox_inches='tight')

if __name__ == "__main__":

    urls = [
        "https://fbref.com/en/comps/12/La-Liga-Stats",          # La Liga (ESP)
        "https://fbref.com/en/comps/9/Premier-League-Stats",    # Premiere League (ENG)
        "https://fbref.com/en/comps/11/Serie-A-Stats",          # Serie A (ITA)
        "https://fbref.com/en/comps/13/Ligue-1-Stats",          # Ligue 1 (FRA)
        "https://fbref.com/en/comps/20/Bundesliga-Stats",       # Bundesliga (ALE)
        "https://fbref.com/en/comps/23/Eredivisie-Stats"        # Eredivisie (NED)
    ]

    leagues = [
        'La Liga (ESP)', 
        'Premiere League (ENG)', 
        'Serie A (ITA)', 
        'Ligue 1 (FRA)',
        'Bundesliga (ALE)',
        'Eredivisie (NED)'
    ]

    GenerateFullClassificationPNGFigures(urls, leagues, 2, 3)
    GenerateClassificationPNGFigures(urls, leagues)
    GenerateFullGoalsForVsGoalsAgaintstPNGFigures(urls, leagues, 2, 3)
    GenerateGoalsForVsGoalsAgaintstPNGFigures(urls, leagues)