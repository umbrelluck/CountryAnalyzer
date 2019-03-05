"""
Module provides easier collection of data and hides those ugly in-function calls
"""
import gdeltAPI
import analyzer

location = ""


def tone_chart(loc=None):
    """
    Easier analyzer.getInfo()
    :param loc: str
    :return: tuple/list
    """
    global location
    if not location:
        location = loc if loc else gdeltAPI.getLocation()
    return analyzer.getInfo(gdeltAPI.transQuery(location))


def timeline_source_country(loc=None, inter=False, base=(0, 0.1)):
    """
    Easier analyze.compareInterest()
    :param loc: str
    :param inter: bool
    :param base: list
    :return: bool/int
    """
    global location
    if not location:
        location = loc if loc else gdeltAPI.getLocation()
    return analyzer.compareInterest(
        analyzer.getInfo(gdeltAPI.transQuery(location, mode="TimelineSourceCountry"),
                         mode="TimelineSourceCountry"), location, base, inter=inter)
