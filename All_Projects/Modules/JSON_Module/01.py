import json
data='{"1st_name":"Anirban","2nd_name":"Sucho"}'
print(data)
parsed=json.loads(data)
print(parsed['1st_name'])
print(parsed['2nd_name'])

#Task 1 - json.load?


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
# json make its compatible for javascript as like here False is small in java script
# and here in python it's capital so it'll make it small like false
jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps
