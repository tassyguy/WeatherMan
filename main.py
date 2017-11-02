from darksky import forecast
from datetime import date, timedelta

ATLANTA = 33.7537, 84.3863

weekday = date.today()
with forecast('7a078e9b0afd5187b96a5b60641343bc', *ATLANTA) as atlanta:
    print(atlanta.daily.summary)
    for day in atlanta.daily:
        day = dict(day = date.strftime(weekday, '%a'),
                   sum = day.summary,
                   tempMin = day.temperatureMin,
                   tempMax = day.temperatureMax
                   )
        print('{day}: {sum} Temp range: {tempMin} - {tempMax}'.format(**day))
        weekday += timedelta(days=1)