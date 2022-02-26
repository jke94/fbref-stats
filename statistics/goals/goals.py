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
import random

class Goals:
    def __init__(self, urls, leagues):
        self.urls = urls
        self.leagues = leagues

    def GenerateFullGoalsForVsGoalsAgainstPNGFigures(self, rows, columns):

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
        figure_full.suptitle('Goals for (GF) Vs Goals against (GA) (Twitter: @JaviKarra94)')

        dataframes = []
        plots = []

        for item in range(0, len(self.urls)):
            dfs = pd.read_html(self.urls[item])
            dataframes.append(dfs[0]) # Get clasificacion table league dataframe

        # Create plots
        for i in range(0, rows):
            for j in range(0, columns):
                plots.append(dataframes[j * rows + i].plot(x="Squad", y=["GF","GA"], kind="bar", ax=axs[i,j], title = self.leagues[j * rows + i], xlabel = "Teams", ylabel = "Goals"))

        for item in (range(0, len(plots))):
            plots[item].grid(axis='y', linestyle='--')

        figure_full.tight_layout()
        figure_full.savefig(os.path.join('.\Goals', 'AllLeagues'), bbox_inches='tight')

    def GenerateGoalsForVsGoalsAgainstPNGFigures(self):

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

        for item in range(0, len(self.urls)):

            dfs = pd.read_html(self.urls[item])
            clasificacion = dfs[0]
            plot = clasificacion.plot(x="Squad", y=["GF","GA"], kind="bar", xlabel ="Teams", ylabel = "Goals")
            fig = plot.get_figure()
            fig.savefig(os.path.join('.\Goals', self.leagues[item].strip()), bbox_inches='tight')

    def GeneratePlotWithGoalsAndAssistsInSeveralLeagues(self):
        
        s = 'A0B123456789CDEF'
        colors = ["#"+''.join([random.choice(s) for i in range(6)])
                        for j in range(len(self.urls))]
        fig, ax = plt.subplots()

        for i in  range(0, len(self.urls)):
            dfs = pd.read_html(self.urls[i])
            df = dfs[2]

            dataframe= df['Performance'][['Gls','Ast']].join(df['Unnamed: 0_level_0']['Squad'])
            dataframe.plot(x='Gls', y='Ast', kind='scatter', ax=ax, color=colors[i], xlabel = "Goals", ylabel = "Assists")
        
        ax.grid(axis='y', linestyle='--')
        ax.grid(axis='x', linestyle='--')
        ax.legend(self.leagues)

        fig.suptitle('Goals and assists (Twitter: @JaviKarra94)')
        fig.savefig('Gls+Ast', dpi=900, bbox_inches='tight')