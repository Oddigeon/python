import json

try:
    with open('./exercise6/input.txt', 'r') as file:
        data = file.read()
        print(json.loads(data))
except:
    print('error') 