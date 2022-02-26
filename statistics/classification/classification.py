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
import logging
from datetime import datetime

class Classification:
    
    def __init__(self, urls, leagues):

        self.__date = ''.join([datetime.now().strftime("%m-%d-%Y"), '.log'])
        self.urls = urls
        self.leagues = leagues
        
        self.__InitializeLogging()

    def __InitializeLogging(self, logs_directory='.\logs'):

        """Initialize logging directory and logging file.

        Parameters
        ----------
        logs_directory : string
            Logs directory.
        log_name : string
            Log name directory.

        """
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        logging.basicConfig(
            filename=os.path.join(logs_directory, self.__date), 
            encoding='utf-8',
            level=logging.INFO)

    def GenerateClassificationPNGFigures(self):

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

        for item in range(0, len(self.urls)):

            dfs = pd.read_html(self.urls[item])
            clasificacion = dfs[0]
            file = os.path.join('.\Classification', self.leagues[item].strip())

            plot = clasificacion.plot(x="Squad", y=["Pts"], kind="bar", xlabel ="Teams", ylabel = "Points")
            fig = plot.get_figure()
            fig.savefig(file, bbox_inches='tight')
        
            logging.info('Created file: %s', file)

    def GenerateFullClassificationPNGFigures(self, rows, columns):

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

        for item in range(0, len(self.urls)):        
            dfs = pd.read_html(self.urls[item])
            dataframes.append(dfs[0]) # Get clasificacion table league dataframe

        # Create plots
        for i in range(0, rows):
            for j in range(0, columns):
                plots.append(dataframes[j * rows + i].plot(x="Squad", y=["Pts"], kind="bar", ax=axs[i,j], title = self.leagues[j * rows + i], xlabel = "Teams", ylabel = "Points"))        

        for item in (range(0, len(plots))):
            plots[item].grid(axis='y', linestyle='--')

        figure_full.tight_layout()
        figure_full.savefig(os.path.join('.\Classification', 'AllLeagues'), bbox_inches='tight')


