import requests
from bs4 import BeautifulSoup
from time import sleep
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"D:\app\kot\product\instantclient_19_8")

def get_html(url, headers):
    response = requests.get(url, headers=headers, timeout=25)

    if not response.ok:  # .status_code == 200:
        print(f'Code: {response.status_code}, url: {url}')
    return response



def get_data(id):


    url = f'https://auto.ria.com/search/?indexName=auto,order_auto,newauto_search&plateNumber.length.gte=1&price.currency=1&abroad.not=-1&custom.not=-1&size=100&page={id}'
    #url = f'https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&plateNumber.length.gte=1&region.id[0]=13&price.currency=1&abroad.not=-1&custom.not=-1&size=100&page={id}'
    #url = f'https://auto.ria.com/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&region.id[0]=13&price.currency=1&sort[0].order=price.asc&abroad.not=0&custom.not=1&size=10000&page={id}'
    print(url)

    headers = {
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0.0",

        "Cookie": "descriptionHidden=1; ab_inspector=1; ui=5f3d674075d69def; test_new_features=117; advanced_search_test=42; showNewFeatures=7; PHPSESSID=4UeWpA73umx9rI5OPu-X7CGopPS7DOtK; showNewNextAdvertisement=10; gdpr=1; PHPSESSID=labWhSYeD5Dt6ek1zuyX-Ag4dd3-HrxO; promolink2=4"
   }


    html = get_html(url, headers)

    soup = BeautifulSoup(html.text, 'lxml')
    #print(soup)

    # Html_file = open('hhhhhhhhh.html', 'w', encoding='utf-8')
    # Html_file.write(html.text)
    # Html_file.close()

    spisok = soup.find_all('section', class_='ticket-item new__ticket t')
    spisok = spisok+soup.find_all('section', class_='ticket-item new__ticket t paid')

    # print(spisok)

    i = 1
    for zapis in spisok:
        if i == 1:
            try:
                url = zapis.find('a' , class_='m-link-ticket').get('href').strip()
                id = zapis.get('data-advertisement-id').strip()
            except:
                 id='-'

            try:
                dat = zapis.find('div' , class_= 'footer_ticket').text.strip()
            except:
                 dat = ''

            try:
                nom = zapis.find('span', class_='state-num ua').text.strip()
                nom = nom.split(' ')[0]+nom.split(' ')[1]+nom.split(' ')[2]
            except:
                nom = ''

            try:
                vin = zapis.find('span', class_='label-vin').text.strip()
                vin = vin.split(' ')[0]
            except:
                try:
                    vin = zapis.find('span', class_='vin-code').text.strip()
                    vin = vin.split(' ')[0]
                except:
                    vin=''

            try:
                mod = zapis.find('span', class_='blue bold').text.strip()
            except:
                mod = ''

            try:
                cost = zapis.find('div', class_='price-ticket').get('data-main-price').strip()
            except:
                cost = ''

            try:
                location = zapis.find('li' , class_="item-char view-location").text.strip()
            except:
                location = ''


            html = get_html(url, headers)
            page = BeautifulSoup(html.text, 'lxml')

            try:
                phone =  page.find('span' , class_="phone bold").get("data-phone-number").strip().replace(' ', '').replace('(', '').replace(')', '')
            except:
                phone = ''

            try:
                saller = page.find('h4' , class_="seller_info_name").text.strip()
            except:
                saller = ''

            try:
                fc_book = page.find_all('div' , class_='item_inner')[3].find('a').get('href').strip().split('golink/?')[1]
            except:
                fc_book = ''

            connection = cx_Oracle.connect('don', 'don', 'IIPS')
            curs = connection.cursor()

            if id != '-':
                curs.execute(
                """
                    select id from  kosta.AUTO_RIA 
                          where id = :id 
                """,
                id = id
                )

                data = curs.fetchall()

                if not data:
                    curs.execute(
                    """
                        insert into kosta.AUTO_RIA 
                            (id, mod, nom, vin, url, text1, text2, phone, dat, saller, fc_book)
                            values 
                            (:id, :mod, :nom, :vin, :url, :text1, :text2, :phone, :dat, :saller, :fc_book)
                     """,
                    id = id,
                    mod = mod,
                    nom = nom,
                    vin = vin,
                    url = url,
                    text1 = cost,
                    text2 = location,
                    phone = phone,
                    dat = dat,
                    saller=saller,
                    fc_book=fc_book

                )
                curs.close()
                connection.commit()
                connection.close()

def main():
    #239
    for i in range(0, 375):
        get_data(i)



if __name__ == '__main__':
    main()