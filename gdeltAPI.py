import json
import urllib.request

baseURL = "https://api.gdeltproject.org/api/v2/doc/doc?query="


def is_validLocation(loc):
    with open("databases/countries.json", encoding="utf-8", errors="replace") as countries:
        for country in json.load(countries):
            if loc == country["country"].lower():
                break
        else:
            with open("databases/cities.json", encoding="utf-8", errors="ignore") as cities:
                for city in json.load(cities):
                    if loc == city["name"].lower():
                        break
                else:
                    return False
    return True


def getLocation():
    print("Please enter full country name (United States not USA or US) or city here")
    location = input(" ==> ").lower()
    while not is_validLocation(location):
        print(
            "Your input is incorrect or we can`t find such location.\nIf you are sure everything "
            "is ""right, press \'Enter\'")
        location = input(" ==> ").lower()
        if location == "":
            break
    return location


def transQuery(query, mode="tonechart", themes=[None]):
    for theme in themes:
        tmp_theme = "theme:" + theme if theme else ""
        requestURL = baseURL + str(query if len(
            query.split()) == 1 else '\"' + query + '\"') + "&mode=" + mode + "&format=json"
        request_result = urllib.request.urlopen(requestURL).read().decode("utf-8")
        request_result = json.loads(request_result)
        yield request_result[mode]


if __name__ == "__main__":
    q = getLocation()
    for elem in transQuery(q):
        print(elem)
