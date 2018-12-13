import json, urllib.request
import pandas as pd

# Reading the JSON data from the provide URL 
url = "http://mysafeinfo.com/api/data?list=englishmonarchs&format=json"
with urllib.request.urlopen(url) as response :
    data = response.read()

data = json.loads(data)
df = pd.DataFrame.from_dict(data, orient = 'columns')
cities = df.cty.unique()
houses = df.hse.unique()

house_output = {}
overall_output = {}
for city in cities:
    for house in houses:
        name_list = []
        for item in data:
            if (item['hse'] == house) & (item['cty'] == city):
                name_list.append(item['nm'])
        house_output.update({house:name_list})
    overall_output.update({city:house_output})

print(overall_output)


