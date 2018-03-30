import json
from pprint import pprint
import requests

try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO

def get_data():
    url = 'https://api.thingspeak.com/channels/462494/feeds/last.json?api_key=BB9R7LUMFJN7E8SB&results=500'
    res = requests.get(url)
    data = json.loads(res.text)
    return data
    # for row in reader:
    #     print('\t'.join(row))
# data = json.load(res.text)
# pprint(data)

if __name__ == '__main__':
    get_data()
