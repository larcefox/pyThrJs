import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs

class Platform_manager:
    '''Class fore save objects in list
    it mixed in Platform and can be call from Platform.manager'''
    platform_list = []

    def platform_list_append(self, platform_class):
       self.platform_list.append(platform_class)

    def clear_platform_list(self):
        self.platform_list.clear()

    def get_platform_list(self):
        return self.platform_list


class Platform(Platform_manager):
    '''Main platfor class'''
    manager = Platform_manager()

    def __init__(self, url:str):
        self.url = url 
        response = requests.get(self.url)
        self.soup = bs(response.content, 'html.parser')
        self.hash = self.soup.html.__hash__()

    def links(self):
        a_tags = self.soup.find_all('a') 
        links = []
        for tag in a_tags:
            if urlparse(tag['href']).scheme:
                links.append(tag['href'])
        return links

    def inner_links(self):
        return list(
                filter(lambda link: urlparse(self.url).netloc in urlparse(link).netloc, self.links())
                )

    def outer_links(self):
        return list(
                filter(lambda link: urlparse(self.url).netloc not in urlparse(link).netloc, self.links())
                )

    @property
    def size(self):
        size_max_value = 100000
        real_x = len(tuple(self.soup.html.descendants))
        real_y = len(self.soup.html.text.splitlines())
        return (real_x if real_x < size_max_value else size_max_value,
                real_y if real_y < size_max_value else size_max_value)

    def generate_platforms(self):
        for link in self.links():
            Platform_fabric.create(link)
        return self.manager.get_platform_list()


class Platform_fabric:
    '''Class for creation platforms'''
    @staticmethod
    def create(url):
        platform = Platform(url)
        platform.platform_list_append(platform)
        return platform



if __name__ == '__main__':
    platgorm = Platform_fabric.create('http://mail.ru')
    print(platgorm.size())
