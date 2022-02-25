__author__ = "Javier Carracedo (@JaviKarra94)"
__copyright__ = "Copyright (c) 2022 Javier Carracedo"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Javier Carracedo"
__twiter__ = "@JaviKarra94"
__status__ = "Production"

from statistics.classification import classification
from statistics.goals import goals

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

    c = classification.Classification(urls=urls, leagues=leagues)
    c.GenerateClassificationPNGFigures()

    g = goals.Goals(urls=urls, leagues=leagues)
    g.GenerateGoalsForVsGoalsAgainstPNGFigures()