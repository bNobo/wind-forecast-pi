# ./get-forecast.sh | python3 ./get-forecast.py
import sys, json, datetime;

max_allowed_speed = 20
maxspeed = 0

weathers = json.load(sys.stdin)['weather']
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
print(tomorrow)

for weather in weathers:
	date = datetime.datetime.strptime(weather['date'], '%Y-%m-%d').date()
	print(date)
	if date == tomorrow:
		hourlies = weather['hourly']
		windspeeds = set([int(data['windspeedKmph']) for data in hourlies])
		print(windspeeds)
		maxspeed = max(windspeeds)
		break

print(maxspeed)

if maxspeed > max_allowed_speed:
	print("wind is too strong")


#print(weathers)

