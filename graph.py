#!/usr/bin/python3

from pprint import pprint
from bs4 import BeautifulSoup, element
import requests


response = requests.get('https://www.google.com/search?q=rambler&oq=rambl&aqs=chrome.0.0i131i433i512j69i57j0i131i433i512l4j0i512j46i199i465i512j0i512l2.7051j0j1&sourceid=chrome&ie=UTF-8')
soup = BeautifulSoup(response.content, 'html.parser')

html_map = {}
tags = soup


def get_map():

    for tag in tags.descendants:
        if isinstance(tag, element.Tag):

            if tag.name in html_map:
                html_map[tag.name][tag.__hash__()] = list(
                        child_tag.__hash__() for child_tag in tag.find_all()
                        ) 
            else:
                html_map[tag.name] = {
                        tag.__hash__(): list(child_tag.__hash__() for child_tag in tag.find_all())
                        }

    return html_map

if __name__ == "__main__":
    print(get_map())
