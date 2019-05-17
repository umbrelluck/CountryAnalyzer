"""
Module with country class and functions to calculate stable stats
"""
from helper import tone_chart, timeline_source_country


class CountriesADT:
    """ADT for countries"""

    def __init__(self, stable_countries_names):
        """
        Initialization of the class
        :param stable_countries_names: list
        """
        self.countries = []
        self._stable(stable_countries_names)

    def append(self, elem):
        self.countries.append(elem)

    def __len__(self):
        return len(self.countries)

    def __iter__(self):
        return self.countries.__iter__()

    def _stable(self, stable_countries_name):
        """
        Fills ADT with countries
        :param stable_countries_name: list
        :return: None
        """
        print("Pre-analyzing world, this can take up to 20 minutes...\n")
        for country in stable_countries_name:
            print(country + ": status - started", end="")
            neg, neu, pos = tone_chart(loc=country)
            interest = timeline_source_country(loc=country, inter=True)
            # print(neg, neu, pos, interest, end=" ")
            self.append(Country(country, neg, neu, pos, interest))
            print("/DONE")
        print(
            "\nPre-analyzing completed. All data is collected. You are ready to start your "
            "search.\n")

    def stability(self):
        """
        Calculates stable stats
        :return: dict
        """
        mood, inter = [0, 0, 0], 0
        for country in self:
            for i in range(3):
                mood[i] += country.emotions[i]
            inter += country.interest
        length = len(self)
        return {"mood": list(map(lambda x: x / length, mood)), "interest": inter / length}


class Country:
    """
    Basic implementation of a country with mood and interest
    """

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
