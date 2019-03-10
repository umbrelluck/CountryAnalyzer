"""
Module with country class and functions to calculate stable stat
"""
from helper import tone_chart, timeline_source_country


class Country:
    """
    Basic implementation of a country with mood and interest
    """
    countries = []

    def __init__(self, name, negative, neutral, positive, interest):
        """
        Initialization of a country class
        :param name: str
        :param negative: float
        :param neutral: float
        :param positive: float
        :param interest: float
        """
        self.name = name
        self.emotions = [negative, neutral, positive]
        self.interest = interest
        self.countries.append(self)

    def stable(self):
        """
        Calculate stable stats
        :return: list
        """
        mood, inter = [0, 0, 0], 0
        for country in self.countries:
            for i in range(3):
                mood[i] += country.emotions[i]
            inter += country.interest
        length = len(self.countries)
        return {"mood": list(map(lambda x: x / length, mood)), "interest": inter / length}


#  CHANGE best_countries!!!!
def stability():
    print("Pre-analyzing world, this can take up to 20 minutes...\n")
    best_counties = ["Grenada", "Brunei", "Seychelles", "Kuwait", "Antigua and Barbuda",
                     "Montenegro", "Greece", "Mongolia", "Trinidad and Tobago", "Oman", "Bulgaria",
                     "Hungary", "Bahamas", "Panama", "Romania", "Croatia", "Barbados", "Qatar",
                     "Argentina", "Latvia", "Italy", "Costa Rica", "Estonia",
                     "United Arab Emirates", "Slovakia", "Poland", "Spain", "Chile", "Mauritius",
                     "Lithuania", "Czech Republic", "United States", "Malta", "South Korea",
                     "Uruguay", "Japan", "United Kingdom", "France", "Singapore", "Slovenia",
                     "Belgium", "Portugal", "Austria", "Netherlands", "Germany", "Canada",
                     "New Zealand", "Sweden", "Australia", "Luxembourg", "Ireland", "Iceland",
                     "Denmark", "Switzerland", "Norway", "Finland"]
    for country in best_counties:
        print(country + ": status - started", end="")
        neg, neu, pos = tone_chart(loc=country)
        interest = timeline_source_country(loc=country, inter=True)
        # print(neg, neu, pos, interest, end=" ")
        ct = Country(country, neg, neu, pos, interest)
        print("/DONE")
    print("\nPre-analyzing completed. All data is collected. You are ready to start your search.\n")
    return ct.stable()
