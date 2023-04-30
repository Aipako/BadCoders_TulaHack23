import requests
from bs4 import BeautifulSoup
import telebot  # pip install pyTelegramBotAPI

import validators # Поможет отслеживать URL ----  pip install validators 

global current_name
global current_price 
global data


# Инициализация бота
bot = telebot.TeleBot('6064462273:AAHvSQZLOS42xhBsTYsl4Gt08olbYgeSw7U')
@bot.message_handler(commands=['start'])


# Обработчик команды /start
def start(message):
    bot.send_message(message.from_user.id,
                             "Привет, {0}! Я могу помочь тебе найти более выгодную цену на товары на n-katalog. Просто отправь мне сообщение по шаблону \"*Найди: *_наименование товара_\" или отправь ссылку на товар, и я начну мониторить цену на этот товар.".format(message.from_user.first_name), parse_mode='markdown')
    bot.register_next_step_handler(message, get_massage_from_user)
    

# Обработчик текстового сообщения
@bot.message_handler(content_types=['text'])

def get_massage_from_user(message):
    request_string_list=message.text.split()
    list_length = len(request_string_list)

    search_key_words = ['Найди', 'найди', 'Найди:', 'найди:']          #----------------------------------- КЛЮЧЕВЫЕ СЛОВА ДЛЯ ЗАПУСКА ЗАПРОСА
    
    print("Кол-во слов в запросе - "+str(list_length))
    print (request_string_list)
    print ("request_string_list[0] -- "+ request_string_list[0])
    

    product_name=""
    global current_name
    global current_price

    # Убираем "Найди:" из запроса и пишем название товара в product_name
    i=0
    for word in request_string_list:
        if i != 0:
           product_name += str(request_string_list[i])
           print (product_name)
           if i != list_length - 1:
               product_name += " "
        i+=1
    
    print ("|"+product_name+"|")

    # Отлавливаем запрос по ключевым словам
    

    i=0
    for key_word in search_key_words:
      print("key_word="+key_word)
      if request_string_list[0] != key_word:
          i+=1
          if i == list_length:
                                                                    # Проверка на URL
              if validators.url(message.text) == True:
                  bot.send_message(message.from_user.id,
                             "Веду поиск по товару, указанному по ссылке: {0}".format(message.text) )
                  search_product_url(message)
                  break
              else:
                 bot.send_message(message.from_user.id,
                             "Введен неверный запрос! Пожалуйста, отправь сообщение в формате \"*Найди: *_наименование товара_\".", parse_mode='markdown')
           
      else:
         bot.send_message(message.from_user.id,
                             "Ищу по запросу \"{0}\"".format(product_name))
         current_name = product_name                                   # Записываем запрос в current_name
         print("current_name-"+current_name)
         i=0
         search_product_no_url(message)
         break
         
         
      
    

     # ищем товар по url                                                                                   ##########################################################################################



def search_product_url (message):
    url=message.text
    print("Перешел в search_product_url")
    nkatalog_price = get_nkatalog_price(url)
    product_name = get_nkatalog_name(url)

   # wildberries_price = get_wildberries_price(product_name)

    if nkatalog_price == None:
        bot.send_message(message.from_user.id,
                                 text="К сожалению, я не смог найти {0} на n-katalog.".format(product_name))
    else:
        bot.send_message(message.from_user.id,
                                 text="Цена на {0} на n-katalog: {1} руб.".format(product_name, nkatalog_price))



        #                            no_url            Ищем товар по запросу "Найди: наименование товара"   ##########################################################################################

def search_product_no_url (message):
    
    print("Перешел в search_product_no_url")
    product_name = message.text
    nkatalog_price = get_nkatalog_name_no_url(product_name)
  

   # wildberries_price = get_wildberries_price(product_name)

    if nkatalog_price == None:
        bot.send_message(message.from_user.id,
                                 text="К сожалению, я не смог найти {0} на n-katalog.".format(product_name))
    else:
        bot.send_message(message.from_user.id,
                                 text="Цена на {0} на n-katalog: {1} руб.".format(product_name, nkatalog_price))



         # Функция для получения цены на товар на nkatalog
def get_nkatalog_price(message):
 
    url=message

    print("Перешел в get_nkatalog_price------------------------\n\n")
    print("Ссылка на товар-- "+url+"\n")
    response = requests.get(url)
    
    
    soup = BeautifulSoup(response.content, 'html.parser') 
    print(soup.prettify())
   
    try:
        
        price = soup.find('span', {'itemprop':'lowPrice'}).text.strip()
        print("\n\n------------------------------------------------Найденная цена товара: " +price)
        return price
    except:
        return None

         # Функция для получения имени товара на n-katalog

def get_nkatalog_name(message):
    url = message
    print("Перешел в get_nkatalog_name------------------------\n\n")
    print("Ссылка на товар-- "+url+"\n")
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
    try:
        product_name = soup.find('h1', {'class':'title-for-page'}, {'itemdrop':'name'}).text.strip()

        
        print("\n\n---------------------------------Найденное имя товара: " +product_name)
        return product_name
    except:
        return None

    # Функция для получения цен на товар по поиску по запросу на n-katalog 


    #    Добавить цикл с запросом первых 10 строк по поиску                         !
    #    Настроить корректное извлечение цены                                       !
    #    изменить формат вывода данных, например:   Товар - цена                    !

def get_nkatalog_name_no_url(message):
    global current_name
    print("Перешел в get_nkatalog_price_no_url------------------------\n\n")
    print("current_name-"+current_name)
    product_name=current_name
    url = 'https://n-katalog.ru/search?keyword={0}'.format(product_name)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
    try:
        product_name = soup.find('span', {'class': 'u'}).text.strip()
        price = soup.find('a', {'href': '/product/apple-iphone-13-pro-max-1tb'},{'span'}).text.strip()
        return product_name
    except:
        return None

                                       ########################################################################################

bot.infinity_polling()
