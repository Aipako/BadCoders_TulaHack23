from selenium import webdriver
from bs4 import BeautifulSoup

product_name=""
product_price=""
# Запуск браузера и открытие страницы поисковой выдачи Яндекса
driver = webdriver.Chrome()
driver.get("https://yandex.ru/search/?text=iphone+13")




# Получение HTML-кода страницы и извлечение списка товаров
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
items_prices = soup.select("span.PriceValue")
items_links = soup.select("a")
items_names = soup.select(".organic .organic__url")
print(items_links)
prices=[]
names=[]
markets=[]
links=[]

# Обход списка товаров и извлечение информации о каждом товаре


print("------------------Наш запрос на ссылки----------------")

    #listing = soup.find("div", {"class": "listing-container"})

domain_element = soup.find_all("div", {"class": "Prbb6dcf86Item-Domain"})
print("\n\ndomain_element:\n")
print(domain_element)



i=0
for item in items_links:
    if i >= 10:
        break

    domain_correct=" ".join(element.text.strip().split() for element in domain_element)
    print("\n\ndomain_correct:\n")
    print(domain_correct)
   # domain_correct=" ".join(element.replace("Выпадающее меню", "") for element in domain_element)
    i+=1

markets.extend(domain_correct)
print("\n\nmarkets:\n")
print(markets)


print("------")
    #domain_correct = domain.replace("Выпадающее меню", "")
    

link_element = soup.find_all('a', {"class": "Link Link_theme_outer"})
i=0
for item in items_links:
    if i >= 10:
        break
    link_url = "".join(element['href'] for element in link_element) 
    i+=1

links.extend(link_url)

print("\n\nlinks:\n")
print(links)

    #link_element = soup.find('a')
    #link_url = link_element['href']
    #print(link_url)


    #domain_element = soup.find("div", {"class": "Prbb6dcf86Item-Domain"})
    #domain = domain_element.text.strip()
    #print(domain)
    
i=0
for item in items_names:
    if i >= 10:
        break
    
    
    name=item.select("b")[:2]
    name_correct=" ".join(element.text.strip() for element in name)
    names.append(name_correct)
    i+=1
    #product_name_elements = item.select_one("b")[:2]
   # names[i] = " ".join(element.text.strip() for element in product_name_elements)
    

i=0

print("\n\n----==============================================================------\n\n")
print(items_prices)
for item in items_prices:
    if i >= 10:
        break
    print("\nPrice:")
    print(item.select_one("span.A11yHidden"))
    try:
        price = item.select_one("span.A11yHidden").text.strip()
    except:
        price = item.text.strip()
    prices.append(price)
    i+=1
   
print(names)
print(markets)
print(prices)
print(links)

    # Вывод информации о товаре на экран
b=0
for i in range (10):
    if b >= 10:
        break
    
    print(f"Название товара: {names[b]}")
    print(f"Магазин: {markets[b]}")
    print(f"Цена товара: {prices[b]}")
    print(f"Ссылка: {links[b]}")
    b+=1
    
    
    
# Закрытие браузера

prices=[]
names=[]
markets=[]
links=[]

driver.quit()
input()