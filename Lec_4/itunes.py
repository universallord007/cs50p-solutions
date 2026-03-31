import json
import requests
import sys 

if len(sys.argv) != 2 :
    sys.exit("Please provide a song name as an argument.")


response =requests.get("https://itunes.apple.com/search?entity=song&limit=15&term="+sys.argv[1])
# print(json.dumps(response.json(),indent=2))


op = response.json()
for result in op["results"] :
    print(result["trackName"],"by",result["artistName"])