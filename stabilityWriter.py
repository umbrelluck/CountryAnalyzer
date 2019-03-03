import country
import datetime
import json
import sys

try:
    with open("databases/stability.txt", "r") as stability_file:
        now = int(datetime.datetime.now().strftime("%U"))
        if now - int(stability_file.readline()) > 1:
            print("Yor data is seemed to be outdated. Would you like to update it? [Y/n]")
            ans = input(" >>> ")
            if ans in ["y", "Y", ""]:
                stability = country.stability()
                print("Data is updated")
            else:
                stability = json.loads(stability_file.readline())
        else:
            stability = json.loads(stability_file.readline())
except Exception:
    with open("databases/stability.txt", "w") as stability_file:
        print("It seems you don`t have required data. Would you like to upload it? [Y/n]")
        ans = input(" >>> ")
        if ans in ["y", "Y", ""]:
            stability_file.write(datetime.datetime.now().strftime("%U")+'\n')
            stability = country.stability()
            json.dump(stability, stability_file)
            print("Data is loaded")
        else:
            sys.exit()
print("You are ready to start your search")
