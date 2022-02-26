__author__ = "Javier Carracedo (@JaviKarra94)"
__copyright__ = "Copyright (c) 2022 Javier Carracedo"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Javier Carracedo"
__twiter__ = "@JaviKarra94"
__status__ = "Production"

from statistics.classification import classification
from statistics.goals import goals
from statistics.constants import FbrefUrl, League

if __name__ == "__main__":

    c = classification.Classification(urls=FbrefUrl.URLS, leagues=League.LEAGUES)
    c.GenerateClassificationPNGFigures()
    c.GenerateFullClassificationPNGFigures(3,2)

    g = goals.Goals(urls=FbrefUrl.URLS, leagues=League.LEAGUES)
    g.GenerateGoalsForVsGoalsAgainstPNGFigures()
    g.GenerateFullGoalsForVsGoalsAgainstPNGFigures(3,2)
    g.GeneratePlotWithGoalsAndAssistsInSeveralLeagues()