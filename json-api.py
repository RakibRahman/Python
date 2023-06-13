import json;
import urllib.request, urllib.parse, urllib.error

endPoint = 'https://jsonplaceholder.typicode.com/todos/1'

while True:
    print('retrieving...')
    openUrl = urllib.request.urlopen(endPoint)
    data = openUrl.read().decode()

    try:
        formattedData = json.loads(data)
        if 'userId' in formattedData:
            print(formattedData)
            break;
    except:
        formattedData = None

    if not formattedData or len(formattedData) == 0:
        print('Something went wrong')
        print(formattedData)
        continue;
