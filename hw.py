import requests
from bs4 import BeautifulSoup
import openpyxl
import csv

url = "https://www.kivano.kg"

def get_product_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    full_links = [] 
    home_page = soup.find('div', class_="site-index oh")
    prod_list = home_page.find('div', class_="body-content")
    prod_inner_list = prod_list.find('div', class_="product_vitrina") 
    prod_title = prod_inner_list.find_all('div', class_="product_title") 

    for title in prod_title:
        for links in title.find_all('a', href=True):
            full_links.append(url + links['href']) 

    return full_links

def scrape_product_details(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')

    titles = soup.find('h1').text 
    artikuls = soup.find(attrs={"itemprop": "sku"}).text
    prices = soup.find(attrs={"itemprop": "price"}).text
    likes = soup.find('span', class_="js_like_count").text
    warranty = soup.find('span', attrs={'style': 'font-size: 11px;left: 241px; position: absolute;top: 2px;'}).text.strip()
    infos = soup.find('div', class_="tab-pane fade in active yandex_hide_some").text

    return {
        'titles': titles,
        'artikuls': artikuls,
        'prices': prices,
        'likes': likes,
        'warranty': warranty,
        'infos': infos
    }

def save_to_excel(products):
    wb = openpyxl.Workbook() 
    sheet = wb.active
    sheet["A1"] = "Название"
    sheet["B1"] = "Артикул"
    sheet["C1"] = "Цена"
    sheet["D1"] = "Нравится"
    sheet["E1"] = "Гарантия"
    sheet["F1"] = "Описание"

    for i, item in enumerate(products, start=2):
        sheet[f"A{i}"] = item["titles"]
        sheet[f"B{i}"] = item["artikuls"]
        sheet[f"C{i}"] = item["prices"]
        sheet[f"D{i}"] = item["likes"]
        sheet[f"E{i}"] = item["warranty"]
        sheet[f"F{i}"] = item["infos"]

    wb.save("kivano.xlsx")



def save_to_csv(products, filename="kivano.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Название", "Артикул", "Цена", "Нравится", "Гарантия", "Описание"])

        for item in products:
            writer.writerow([
                item["titles"],
                item["artikuls"],
                item["prices"],
                item["likes"],
                item["warranty"],
                item["infos"]
            ])



product_links = get_product_links(url)
all_products = []

for link in product_links:
    product_details = scrape_product_details(link)
    all_products.append(product_details)

save_to_excel(all_products)
save_to_csv(all_products) 