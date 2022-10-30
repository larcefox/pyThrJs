from urllib.parse import urlparse
from bs4 import BeautifulSoup, element
import requests


class Platform_manager:
    platform_list = []

    def platform_list_append(self, platform_class):
       self.platform_list.append(platform_class)

    def clear_platform_list(self):
        self.platform_list.clear()

    def get_platform_list(self):
        return self.platform_list


class Platform(Platform_manager):

    manager = Platform_manager()

    def __init__(self, page:str) -> None:
        self.page = page
        self.platform = get_platform(self.page)

    @property
    def get_inner_links(self):
        inner_links = set() 
        for link in self.platform['links']:
            if urlparse(self.page).netloc in urlparse(link).netloc:
                if urlparse(link).scheme:
                    inner_links.add(link)
        return tuple(inner_links)

    @property
    def get_outer_links(self):
        outer_links = set() 
        for link in self.platform['links']:
            if urlparse(self.page).netloc not in urlparse(link).netloc:
                if urlparse(link).scheme:
                    outer_links.add(link)
        return tuple(outer_links)

    @property
    def get_size(self):
        return self.platform['size']

    @property
    def get_level(self):
        return len(urlparse(self.page).path.split('/'))

    def generate_inner_childs(self):
        for link in self.get_inner_links:
            Platform_fabric.create(link)

    def generate_outer_childs(self):
        for link in self.get_outer_links:
            Platform_fabric.create(link)


class Platform_fabric:
    @staticmethod
    def create(page):
        platform = Platform(page)
        platform.platform_list_append(platform)
        return platform


#TODO remove this function from class file to lib folder
def get_platform(start_page):

    response = requests.get(start_page)
    soup = BeautifulSoup(response.content, 'html.parser')
    size_multiplyer = 10
    body_size = []
    links = []

    for tag in soup.descendants:
        if isinstance(tag, element.Tag):
            
            if tag.name == 'body': body_size = (
                    max([len(i) for i in tag.text.splitlines()]) / size_multiplyer, 
                    len(tag.text.splitlines()) / size_multiplyer 
                    )
            if tag.has_attr('href'): links.append(tag['href'])

    return {'size': body_size, 'links': links}

if __name__ == '__main__':
    platform_obj = Platform('http://mail.ru')
    print(platform_obj.get_inner_links)
