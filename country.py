"""
Module with country class and functions to calculate stable stat
"""
from helper import tone_chart, timeline_source_country


class Country:
    """
    Basic implementation of a country with mood and interest
    """
    countries = []
    best_stats = [0, 0, 0, 0]

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
        self.__update_stats([negative, neutral, positive], interest)

    def __update_stats(self, mood, interest):
        """
        Update stats when country added
        :param mood: tuple
        :param interest: float
        :return: None
        """
        for i in range(3):
            self.best_stats[i] += mood[i]
            self.best_stats[3] += interest

    def stable(self):
        """
        Calculate stable stats
        :return: list
        """
        best_res = dict()
        length = len(self.countries)
        best_res["mood"] = [elem / length for elem in self.best_stats]
        best_res["interest"] = self.best_stats[3] / length
        return best_res


#  CHANGE best_countries!!!!
if __name__ == "__main__":
    best_counties = ["Belgium", "United States"]
    for country in best_counties:
        neg, neu, pos = tone_chart(loc=country)
        interest = timeline_source_country(loc=country, inter=True)
        ct = Country(country, neg, neu, pos, interest)

    base = ct.stable()["interest"], 0.01
    print(ct.stable())
    neg, neu, pos = tone_chart(loc="Russia")
    print(neg, neu, pos)
    interest = timeline_source_country(loc="Russia", base=base)
    ct = Country("Russia", neg, neu, pos, interest)
    print(ct.interest)
