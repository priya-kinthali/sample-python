import time
import requests

while True:
    response = requests.get('https://api.github.com/repos/actions/python-versions/contents/versions-manifest.json')

    if response.status_code == 429:
        print("Rate limit exceeded")
        break

    time.sleep(1)  # Pause to avoid hitting the rate limit too quickly