filepath = 'data/weather_data_2000'

station_temp_dict = {}

with open(filepath) as fs:
  for line in fs:
    tokens = line.split('|')
    stationno = tokens[0]
    temp = float(tokens[-1])

    if stationno in station_temp_dict:
      if station_temp_dict[stationno] < temp:
        station_temp_dict[stationno] = temp
    else:
      station_temp_dict[stationno] = temp

print(station_temp_dict)

