from glob import glob
from fileinput import input
from csv import DictWriter
import json

# list all the files (absolute paths), in a folder
files = glob('data/weather_data_*')

year_temp_dict = {}

# multiple input resources from where u want to read

with input(files) as fp:
  for line in fp:
    tokens = line.split('|')
    year, temp = tokens[1], float(tokens[-1])

    if year in year_temp_dict:
      if year_temp_dict[year] < temp:
        year_temp_dict[year] = temp
    else:
      year_temp_dict[year] = temp


final_dict = [{'year': year, 'maxtemp': year_temp_dict[year]} for year in year_temp_dict]
'''with open('data/max_temp_yearly.csv', mode='w') as fp:
  writer = DictWriter(fp, fieldnames=['year', 'maxtemp'])
  writer.writeheader()
  writer.writerows(final_dict)'''

with open('data/max_temp_yearly.json', mode='w') as fp:
  json.dump(final_dict, fp)