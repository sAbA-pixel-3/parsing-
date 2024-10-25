from bs4 import BeautifulSoup

file = open("index.html", "r", encoding="utf-8")
html = file.read()

soup = BeautifulSoup(html, "html.parser") 

# main_content = soup.find("div", class_="main-content")

# menu = main_content.find("div", class_="menu")
# # print(menu)
# words = menu.find_all("p", class_="navigator")
# # print(words)
# for word in words:
#     print(word.text)


# main = soup.find("div", class_="main")
# print(main)
# post = main.find("div", class_="post")
# print(post)
# post_inner = post.find("h1", class_="post-iner")
# print(post_inner)
# for post in post_inner:
#     print(post_inner.text)

# post1 = main.find_all("div", class_="post")
# print(post1)
# for post in post1:
#     print(post.text)

# main = soup.find("div", class_="main")
# post1 = main.find_all("div", class_="post")
# for post in post1:
#     print(post.text)


# main = soup.find("div", class_="main")
# post1 = main.find_all("h1", class_="post-iner")
# for post in post1:
#     print(post.text)


# OR
# main = soup.find("div", class_="main")
# post1 = main.find_all("div", class_="post")
# for post in post1:
#     h1 = post.find("h1")


# main = soup.find("div", class_="footer")
# for i in main:
#     print(i.text)



# main = soup.find("div", class_="footer")
# box = main.find("div", class_="box")
# for i in box:
#     p = i.find("p")
#     print(p.text)
#     a = i.find("a")
#     print(a.text)
