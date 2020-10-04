from bs4 import BeautifulSoup
import requests

terms_dict = {"facility":['facility','facilites'], 'department':['branch', 'department','school'], 'hostel':['hostel', 'accomodation']}

def get_links_from_page(html, content):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a_tag in soup.find_all('a', href=True):
        if content in a_tag or content in a_tag.text.lower():
            links.append(a_tag["href"])
    return links

def get_content_from_url(url):
    try:
        return requests.get(url).content
    except requests.ConnectionError as e:
        print("Connection Error. Make sure you are connected to Internet.\n")
        print(str(e))
    except requests.Timeout as e:
        print("Timeout Error")
        print(str(e))

def get_content_by_class(html, classname):
    content = []
    soup = BeautifulSoup(html, "html.parser")
    for name in soup.find_all(class_=classname):
        content.append(name.text)
    return content

def get_content_by_tags(html, tag):
    data = []
    soup = BeautifulSoup(html, "html.parser")
    for name in soup.find_all(tag):
        data.append(name.text)
    return data
