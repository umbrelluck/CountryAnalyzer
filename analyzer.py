"""
Module used for analysis of gdelt data
"""
import copy


def convertDate(date):
    """
    Convert gdelt data to day.month.year
    :param date: str
    :return: str
    """
    tmp = date[:4] + '.' + date[4:6] + '.' + date[6:8]
    return tmp[::-1]


def getInfo(stats, mode="tonechart"):
    """
    Gets base info for computing depending on type of stats
    :param stats: list
    :param mode: str
    :return: tuple/list
    """
    if mode == "tonechart":
        total, negative, neutral, positive = 0, 0, 0, 0
        for stat_by_mood in stats:
            for mood in stat_by_mood:
                total += abs(mood["count"] * mood["bin"])
                if mood["bin"] < -1:
                    negative += mood["count"] * mood["bin"]
                elif -1 <= mood["bin"] <= 1:
                    neutral += mood["count"] * mood["bin"]
                else:
                    positive += mood["count"] * mood["bin"]
        return negative / total, neutral / total, positive / total
    elif mode == "TimelineSourceCountry":
        interest = {}
        for stat in stats:
            for stat_by_country in stat:
                series = stat_by_country["series"]
                data = stat_by_country["data"]
                for elem in data:
                    if elem["value"] != 0:
                        if elem["date"][:8] not in interest:
                            interest[elem["date"][:8]] = [(series, elem["value"])]
                        else:
                            interest[elem["date"][:8]].append((series, elem["value"]))
        return interest


def compareInterest(interest, loc, default, inter=False):
    """
    Compares interest of countries and returns if needed deeper analyze or interest rate
    :param interest: dict
    :param loc: str
    :param default: tuple
    :param inter: bool
    :return: bool/int
    """
    interest_set = copy.deepcopy(interest)
    maxs = {key: [] for key in interest}
    for i in range(3):
        for key, value in interest_set.items():
            tmp_max = {}
            for val in value:
                if tmp_max == {}:
                    tmp_max[key] = val
                elif val[1] > tmp_max[key][1]:
                    tmp_max[key] = val
            for key1, value1 in tmp_max.items():
                maxs[key1].append(value1)
                interest_set[key].remove(value1)
    count = 0
    for key, value in maxs.items():
        # CHANGE 5!!!!
        try:
            if loc in value[0][0].lower() and (
                    (value[0][1] - value[1][1]) - (value[1][1] - value[2][1])) > 5:
                count += 1
        except IndexError:
            continue
    if inter:
        return count / len(maxs)
    return count / len(maxs) > sum(default)


if __name__ == "__main__":
    import gdeltAPI

    res = getInfo(gdeltAPI.transQuery("Belgium", mode="TimelineSourceCountry"),
                  mode="TimelineSourceCountry")
    tmp = compareInterest(res, "Belgium", default=(0, 0.1))
    print(tmp)
