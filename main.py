from time import sleep
from datetime import datetime
import requests

sites = [
    "https://github.com",
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.youtube.com"
]

while True:
    sleep(5)

    status = list(map(requests.get, sites))
    with open("log.txt", "w") as f:
        now = datetime.now()
        for site, s in zip(sites, status):
            f.write(f"{now}: {site} - {s.status_code}\n")
    print("Log updated.")