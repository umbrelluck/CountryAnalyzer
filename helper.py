"""
Module provides easier collection of data and hides those ugly in-function calls
"""
import gdeltAPI
import analyzer


def tone_chart(loc=None):
    """
    Easier analyzer.getInfo()
    :param loc: str
    :return: tuple/list
    """
    if loc is None:
        loc = gdeltAPI.getLocation()
    return analyzer.getInfo(gdeltAPI.transQuery(loc))


def timeline_source_country(loc=None, inter=False, base=(0, 0.1)):
    """
    Easier analyze.compareInterest()
    :param loc: str
    :param inter: bool
    :param base: list
    :return: bool/int
    """
    if loc is None:
        loc = gdeltAPI.getLocation()
    return analyzer.compareInterest(
        analyzer.getInfo(gdeltAPI.transQuery(loc, mode="TimelineSourceCountry"),
                         mode="TimelineSourceCountry"), loc, base, inter=inter)
