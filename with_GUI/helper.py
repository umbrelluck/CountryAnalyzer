"""
Module provides easier collection of data and hides those ugly in-function calls
"""
import gdeltAPI
import analyzer

location = ""


def negative_news_count(loc=None, topics=[None]):
    """
    Counts the number of negative news on topics in themes
    :param loc: str
    :param topics: list/tuple
    :return: tuple
    """
    unique = set()
    count_by_topic, i = {}, 0
    global location
    location = location if location else loc
    location = location if location else gdeltAPI.getLocation()
    for news in gdeltAPI.transQuery(location, themes=topics):
        count = 0
        if news:
            for elem in news:
                if elem['bin'] < -1:
                    count += len(elem['toparts'])
                    for el in elem['toparts']:
                        unique.add((el['title'], el['url']))
                else:
                    break
        count_by_topic[topics[i]] = count
        i += 1
    return count_by_topic, unique


def tone_chart(loc=None):
    """
    Easier analyzer.getInfo()
    :param loc: str
    :return: tuple/list
    """
    global location
    # if not location:
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
    # if not location:
    location = loc if loc else location if location else gdeltAPI.getLocation()
    return analyzer.compareInterest(
        analyzer.getInfo(gdeltAPI.transQuery(location, mode="TimelineSourceCountry"),
                         mode="TimelineSourceCountry"), location, base, inter=inter)


if __name__ == "__main__":
    neg, neu, pos = tone_chart(loc="Brunei")
    inte = timeline_source_country(loc="Brunei", inter=True)
    print(neg, neu, pos, inte)
