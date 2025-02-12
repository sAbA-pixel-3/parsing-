import requests
from bs4 import BeautifulSoup 
import openpyxl

def get_product_links(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    full_links = []
    home_page = soup.find('div', class_="content-wrapper")
    home_list = soup.find('div', class_="listings-wrapper")
    home_title = soup.find_all('div', class_="title")
    for title in home_title:
        for links in title.find_all('a', href=True):
            full_links.append('https://www.house.kg' + links['href'])
    return full_links

def get_detail(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36'
    }
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    date = soup.find('span', class_="added-span").text
    print(date) 
        

if __name__ == "__main__":
    for i in range(1, 255):
        url = f"https://www.house.kg/snyat?page={i}"
        links = get_product_links(url)
        # print(f"Page {i}: {links}")
        for link in links:
            get_detail(link) 