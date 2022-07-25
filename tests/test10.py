import json
import requests

auth = requests.get("https://astralsb.ga/authsadj214912090784102.json").text


auth = json.loads(auth)

whitelistedusernames = auth["whitelistedusernames"]
whitelistedpasswords = auth["whitelistedpasswords"]