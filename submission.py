import requests


url = 'https://lf8q0kx152.execute-api.us-east-2.amazonaws.com/default/computeFitnessScore'

x = requests.post(url, json={"qconfig": "1 4 6 3 0 7 5 2",
                             "userID": 795372,
                             "githubLink": "https://github.com/skyegrey/CognizantCodingChallenge"})

print(x.text)