from bs4 import BeautifulSoup
import requests



def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def get_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    content = soup.find('div', class_ = 'ipc-page-grid ipc-page-grid--bias-left')
    list_m = content.find('ul', class_ = 'ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 kYyDJe compact-list-view ipc-metadata-list--base')
    movies = list_m.find_all('li', class_ = 'ipc-metadata-list-summary-item sc-4929eaf6-0 DLYcv cli-parent')
    for movie in movies:
        right_side =  movie.find('div', class_ = 'ipc-metadata-list-summary-item__c')
        link = right_side.find('a', class_ = 'ipc-title-link-wrapper').get('href')
        title = right_side.find('h3', class_ = 'ipc-title__text')
        full_link = 'https://www.imdb.com' + link
        links.append(full_link)
    return links



def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find('div', class_="ipc-page-content-container ipc-page-content-container--full sc-253ad8fd-0 iFnBOf")
    title_div = main.find('div', class_="sc-70a366cc-0 bxYZmb")
    title = title_div.find('span', class_="hero__primary-text")
    lishki = title.find_all('li', class_="ipc-inline-list__item")
    for li in lishki:
        info = li.text

    scroll = main.find('div', class_="ipc-chip-list__scroller")
    genres = scroll.find_all('a', class_="ipc-chip ipc-chip--on-baseAlt")
    for genre in genres:
        genr = genre.text
    description = main.find('span', class_="sc-fbb3c9a4-0 liSKpp")
    people = main.find_all('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt")
    for p in people:
        director = p.find('li', class_="ipc-metadata-list__item") 
    top_cast = main.find_all('div', class_="sc-cd7dc4b7-7 vCane")
    for cast in top_cast:
        nickname = cast.find_all('span', class_="sc-cd7dc4b7-4 zVTic")
        for nick in nickname:
            print("--------------------------------------------")
            print(cast.text)
            print(nick.text)
        
    






def main():
    URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    html = get_html(URL)
    full_links = get_links(html)
    for link in full_links:
        detail_html = get_html(link)
        get_data(detail_html)


if __name__ == "__main__":
    main()






















    # content = soup.find('div', class_="ipc-page-grid ipc-page-grid--bias-left")
    # list_m = content.find_all('li', class_="ipc-metadata-list-summary-item")
    # for list in list_m:
    # #     description = list.find('div', class_="ipc-html-content-inner-div")
    # #     print(description) 
    #     # iner = list.find('div', class_="ipc-metadata-list-summary-item__c")
    #     # iner1 = iner.find('div', class_="ipc-metadata-list-summary-item__tc")
    #     # iner2 = iner1.find('div', class_="ipc-html-content-inner-div")
    #     # print(iner2)
    #     spans = list.find_all('span')
    #     for span in spans:
    #         director = span.find('span', class_="sc-54004b59-5 fDyTMx")
    #         print(director.text)
