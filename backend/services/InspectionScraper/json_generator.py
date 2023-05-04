import requests
import threading
import json
import time
from bs4 import BeautifulSoup

#################################

def get_links(html: str) -> list:
    links = []
    for link in parsed_html.find_all("a"):
        href = link.get("href")
        if href is not None:
            links.append(href)

    links = [f"https://apps.pittcountync.gov{x}" for x in links if 'Inspection' in x]
    return links

def make_request(url):
    for i in range(5):
        try:
            response = requests.get(url)
            return response
        except:
            time.sleep(5)

def get_html(response):
    return BeautifulSoup(response.content, "html.parser")


def get_map(responses):
    inspection_map = {}
    for response in responses:
        parsed_html = get_html(response)
        
        strong_tag = parsed_html.find("address").strong
        name = strong_tag.text
        table = parsed_html.find_all('table')

        inspection_map[name] = str(table[0])

    return inspection_map

#################################

url = "https://apps.pittcountync.gov/apps/health/restrate/Restaurant/Search/Score?minScore=0&maxScore=100"

response = requests.get(url)
html = response.content

parsed_html = BeautifulSoup(html, "html.parser")

links = get_links(html=parsed_html)

threads = []
responses = []

for link in links:
    thrd = threading.Thread(target=lambda: responses.append(make_request(link)))
    threads.append(thrd)
    thrd.start()

for thrd in threads:
    thrd.join()

inspection_map = get_map(responses)
inspection_map['length'] = len(responses)

with open("bin/inspection_data.json", "w") as outfile:
    json.dump(inspection_map, outfile, indent=4, separators=(", ", ": "))




