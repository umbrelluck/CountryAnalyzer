"""Example of using CountriesADT"""
from country import CountriesADT
if I have file with relevent data and it is not outdated:
    simply read file
elif data is outdated:
    ask permission to update it
else:
    names_list=['name1','name2']  #static for now will improve in future
    countries=CountriesADT(names_list)
    average_data=countries.stability()
    write average_data in file for further use
ask user for country
start research