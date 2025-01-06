from autoscraper import AutoScraper

base_url = 'https://www.kivano.kg/' 
wanted_list = ["Сотовый телефон Google Pixel 9 256GB кремовый", "90980 сом"] 

scraper = AutoScraper()

user = input(
    "T for product titles,\n"
    "P for product prices,\n"
    "B for both: ").strip().lower() 

def title(): 
    print("Product titles: ") 
    result = scraper.build(base_url, [wanted_list[0]]) 
    for want in result:
        print(want) 
     
def price():
    print("Product prices: ")
    result = scraper.build(base_url, [wanted_list[1]]) 
    for want in result:
        print(want)
        
def both():
    print("Product titles & prices: ")
    result = scraper.build(base_url, wanted_list)  
    for want in result:
        print(want) 

if user == "t":
    title()
elif user == "p":
    price()
elif user == "b":
    both()  
else:
    print("Invalid input...\nPlease type one of the options!") 