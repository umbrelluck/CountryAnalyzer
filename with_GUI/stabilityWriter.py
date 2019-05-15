"""Module for working with saved data"""
from country import CountriesADT
import datetime
import json
import sys


def get_stability():
    """
    Creates CountriesADT and for all countries there calculates their average data
    :return: dict
    """
    best_countries = ["Grenada", "Brunei", "Seychelles", "Kuwait", "Antigua and Barbuda",
                      "Montenegro", "Greece", "Mongolia", "Trinidad and Tobago", "Oman",
                      "Bulgaria",
                      "Hungary", "Bahamas", "Panama", "Romania", "Croatia", "Barbados", "Qatar",
                      "Argentina", "Latvia", "Italy", "Costa Rica", "Estonia",
                      "United Arab Emirates", "Slovakia", "Poland", "Spain", "Chile",
                      "Mauritius",
                      "Lithuania", "Czech Republic", "United States", "Malta", "South Korea",
                      "Uruguay", "Japan", "United Kingdom", "France", "Singapore", "Slovenia",
                      "Belgium", "Portugal", "Austria", "Netherlands", "Germany", "Canada",
                      "New Zealand", "Sweden", "Australia", "Luxembourg", "Ireland", "Iceland",
                      "Denmark", "Switzerland", "Norway", "Finland"]
    countries = CountriesADT(best_countries)
    return countries.stability()


try:
    with open("databases/stability.txt", "r") as stability_file:
        now = int(datetime.datetime.now().strftime("%U"))
        if now - int(stability_file.readline()) > 0:
            print(
                "Yor data is seemed to be outdated. Would you like to update it? [Y/n]")
            ans = input(" >>> ")
            if ans in ["y", "Y", ""]:
                raise EOFError
            else:
                stability = json.loads(stability_file.readline())
        else:
            stability = json.loads(stability_file.readline())
except EOFError:
    with open("databases/stability.txt", "w") as stability_file:
        stability_file.write(datetime.datetime.now().strftime("%U") + '\n')
        stability = get_stability()
        json.dump(stability, stability_file)
        print("Data is updated")
except Exception:
    with open("databases/stability.txt", "w") as stability_file:
        print(
            "It seems you don`t have required data. Would you like to upload it? [Y/n]")
        ans = input(" >>> ")
        if ans in ["y", "Y", ""]:
            stability_file.write(datetime.datetime.now().strftime("%U") + '\n')
            stability = get_stability()
            json.dump(stability, stability_file)
            print("Data is loaded")
        else:
            sys.exit()
print("You are ready to start your search\n")
