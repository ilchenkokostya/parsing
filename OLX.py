import requests
from bs4 import BeautifulSoup
from time import sleep
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"D:\app\kot\product\instantclient_19_8")


def get_html(url, headers, cookies):
    response = requests.get(url, headers=headers, cookies=cookies, timeout=25)

    if not response.ok:  # .status_code == 200:
        print(f'Code: {response.status_code}, url: {url}')
        sleep(20)
        response = requests.get(url, headers=headers, cookies=cookies, timeout=25)
        if not response.ok:  # .status_code == 200:
            print(f'Code: {response.status_code}, url: {url}')
            sleep(20)
            response = requests.get(url, headers=headers, cookies=cookies, timeout=25)
            if not response.ok:  # .status_code == 200:
                print(f'Code: {response.status_code}, url: {url}')
                sleep(20)
                response = requests.get(url, headers=headers, cookies=cookies, timeout=25)
                if not response.ok:  # .status_code == 200:
                    print(f'Code: {response.status_code}, url: {url}')

    return response

def get_data(u, id, reg):
    #url = f'https://www.olx.ua/don/?page={id}'
    #url = f'https://www.olx.ua/list/?page={id}'

    # Недвижимость
    if u == 1:
        url = f'https://www.olx.ua/nedvizhimost/{reg}?page={id}'
    if u == 2:
        url = f'https://www.olx.ua/nedvizhimost/kvartiry-komnaty/{reg}?page={id}'
    if u == 3:
        url = f'https://www.olx.ua/nedvizhimost/garazhy-parkovki/{reg}?page={id}'
    if u == 4:
        url = f'https://www.olx.ua/nedvizhimost/doma/{reg}?page={id}'
    if u == 5:
        url = f'https://www.olx.ua/nedvizhimost/posutochno-pochasovo/{reg}?page={id}'
    if u == 6:
        url = f'https://www.olx.ua/nedvizhimost/zemlya/{reg}?page={id}'
    if u == 7:
        url = f'https://www.olx.ua/nedvizhimost/predlozheniya-ot-zastroyshchikov/{reg}?page={id}'
    if u == 8:
        url = f'https://www.olx.ua/nedvizhimost/kommercheskaya-nedvizhimost/{reg}?page={id}'
    if u == 9:
        url = f'https://www.olx.ua/nedvizhimost/nedvizhimost-za-rubezhom/{reg}?page={id}'

    # Транспорт
    if u == 10:
        url = f'https://www.olx.ua/transport/{reg}?page={id}'
    if u == 11:
        url = f'https://www.olx.ua/transport/avtobusy/{reg}?page={id}'
    if u == 12:
        url = f'https://www.olx.ua/transport/vodnyy-transport/{reg}?page={id}'
    if u == 13:
        url = f'https://www.olx.ua/zapchasti-dlya-transporta/{reg}?page={id}'
    if u == 14:
        url = f'https://www.olx.ua/transport/avtomobili-iz-polshi/{reg}?page={id}'
    if u == 15:
        url = f'https://www.olx.ua/transport/moto/{reg}?page={id}'
    if u == 16:
        url = f'https://www.olx.ua/transport/vozdushnyy-transport/{reg}?page={id}'
    if u == 17:
        url = f'https://www.olx.ua/transport/legkovye-avtomobili/{reg}?page={id}'
    if u == 18:
        url = f'https://www.olx.ua/transport/gruzovye-avtomobili/{reg}?page={id}'
    if u == 19:
        url = f'https://www.olx.ua/transport/gruzovye-avtomobili/{reg}?page={id}'
    if u == 20:
        url = f'https://www.olx.ua/transport/spetstehnika/{reg}?page={id}'
    if u == 21:
        url = f'https://www.olx.ua/transport/pritsepy-doma-na-kolesah/{reg}?page={id}'
    if u == 22:
        url = f'https://www.olx.ua/transport/gruzoviki-i-spetstehnika-iz-polshi/{reg}?page={id}'
    if u == 23:
        url = f'https://www.olx.ua/transport/selhoztehnika/{reg}?page={id}'
    if u == 24:
        url = f'https://www.olx.ua/transport/drugoy-transport/{reg}?page={id}'

    # detskiy-mir
    if u == 25:
        url = f'https://www.olx.ua/detskiy-mir/{reg}?page={id}'
    if u == 26:
        url = f'https://www.olx.ua/detskiy-mir/detskaya-odezhda/{reg}?page={id}'
    if u == 27:
        url = f'https://www.olx.ua/detskiy-mir/detskaya-odezhda/{reg}?page={id}'
    if u == 28:
        url = f'https://www.olx.ua/detskiy-mir/detskaya-obuv/{reg}?page={id}'
    if u == 29:
        url = f'https://www.olx.ua/detskiy-mir/detskie-kolyaski/{reg}?page={id}'
    if u == 30:
        url = f'https://www.olx.ua/detskiy-mir/detskie-avtokresla/{reg}?page={id}'
    if u == 31:
        url = f'https://www.olx.ua/detskiy-mir/detskaya-mebel/{reg}?page={id}'
    if u == 32:
        url = f'https://www.olx.ua/detskiy-mir/igrushki/{reg}?page={id}'
    if u == 33:
        url = f'https://www.olx.ua/detskiy-mir/detskiy-transport/{reg}?page={id}'
    if u == 34:
        url = f'https://www.olx.ua/detskiy-mir/kormlenie/{reg}/?page={id}'
    if u == 35:
        url = f'https://www.olx.ua/detskiy-mir/tovary-dlya-shkolnikov/{reg}?page={id}'
    if u == 36:
        url = f'https://www.olx.ua/detskiy-mir/prochie-detskie-tovary/{reg}?page={id}'

    # zapchasti-dlya-transporta
    if u == 37:
        url = f'https://www.olx.ua/zapchasti-dlya-transporta/{reg}?page={id}'
    if u == 38:
        url = f'https://www.olx.ua/zapchasti-dlya-transporta/avtozapchasti-i-aksessuary/{reg}?page={id}'
    if u == 39:
        url = f'https://www.olx.ua/zapchasti-dlya-transporta/shiny-diski-i-kolesa/{reg}?page={id}'
    if u == 40:
        url = f'https://www.olx.ua/zapchasti-dlya-transporta/zapchasti-dlya-spets-sh-tehniki/{reg}?page={id}'
    if u == 41:
        url = f'https://www.olx.ua/zapchasti-dlya-transporta/motozapchasti-i-aksessuary/{reg}?page={id}'
    if u == 42:
        url = f'https://www.olx.ua/zapchasti-dlya-transporta/prochie-zapchasti/{reg}?page={id}'

    # uslugi
    if u == 43:
        url = f'https://www.olx.ua/uslugi/{reg}?page={id}'
    if u == 44:
        url = f'https://www.olx.ua/uslugi/stroitelstvo-otdelka-remont/{reg}?page={id}'
    if u == 45:
        url = f'https://www.olx.ua/uslugi/finansovye-uslugi/{reg}?page={id}'
    if u == 46:
        url = f'https://www.olx.ua/uslugi/perevozki-arenda-transporta/{reg}?page={id}'
    if u == 47:
        url = f'https://www.olx.ua/uslugi/reklama-marketing-pr/{reg}?page={id}'
    if u == 48:
        url = f'https://www.olx.ua/uslugi/nyani-sidelki/{reg}?page={id}'
    if u == 49:
        url = f'https://www.olx.ua/uslugi/syre-materialy/{reg}?page={id}'
    if u == 50:
        url = f'https://www.olx.ua/uslugi/krasota-zdorove/{reg}?page={id}'
    if u == 51:
        url = f'https://www.olx.ua/uslugi/oborudovanie/{reg}?page={id}'
    if u == 52:
        url = f'https://www.olx.ua/uslugi/obrazovanie/{reg}?page={id}'
    if u == 53:
        url = f'https://www.olx.ua/uslugi/uslugi-dlya-zhivotnyh/{reg}?page={id}'
    if u == 54:
        url = f'https://www.olx.ua/uslugi/prodazha-biznesa/{reg}?page={id}'
    if u == 55:
        url = f'https://www.olx.ua/uslugi/razvlechenie-foto-video/{reg}?page={id}'
    if u == 56:
        url = f'https://www.olx.ua/uslugi/turizm-immigratsiya/{reg}?page={id}'
    if u == 57:
        url = f'https://www.olx.ua/uslugi/uslugi-perevodchikov-nabor-teksta/{reg}?page={id}'
    if u == 58:
        url = f'https://www.olx.ua/uslugi/avto-moto-uslugi/{reg}?page={id}'
    if u == 59:
        url = f'https://www.olx.ua/uslugi/remont-i-obsluzhivanie-tehniki/{reg}?page={id}'
    if u == 60:
        url = f'https://www.olx.ua/uslugi/setevoy-marketing/{reg}?page={id}'
    if u == 61:
        url = f'https://www.olx.ua/uslugi/yuridicheskie-uslugi/{reg}?page={id}'

    # elektronika
    if u == 62:
        url = f'https://www.olx.ua/elektronika/{reg}?page={id}'
    if u == 63:
        url = f'https://www.olx.ua/elektronika/telefony-i-aksesuary/{reg}?page={id}'
    if u == 64:
        url = f'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/{reg}?page={id}'
    if u == 65:
        url = f'https://www.olx.ua/elektronika/foto-video/{reg}?page={id}'
    if u == 66:
        url = f'https://www.olx.ua/elektronika/tv-videotehnika/{reg}?page={id}'
    if u == 67:
        url = f'https://www.olx.ua/elektronika/audiotehnika/{reg}?page={id}'
    if u == 68:
        url = f'https://www.olx.ua/elektronika/igry-i-igrovye-pristavki/{reg}?page={id}'
    if u == 69:
        url = f'https://www.olx.ua/elektronika/planshety-el-knigi-i-aksessuary/{reg}?page={id}'
    if u == 70:
        url = f'https://www.olx.ua/elektronika/noutbuki-i-aksesuary/{reg}?page={id}'
    if u == 71:
        url = f'https://www.olx.ua/elektronika/tehnika-dlya-doma/{reg}?page={id}'
    if u == 72:
        url = f'https://www.olx.ua/elektronika/tehnika-dlya-kuhni/{reg}?page={id}'
    if u == 73:
        url = f'https://www.olx.ua/elektronika/klimaticheskoe-oborudovanie/{reg}?page={id}'
    if u == 74:
        url = f'https://www.olx.ua/elektronika/individualnyy-uhod/{reg}?page={id}'

    # moda-i-stil
    if u == 75:
        url = f'https://www.olx.ua/moda-i-stil/{reg}?page={id}'
    if u == 76:
        url = f'https://www.olx.ua/moda-i-stil/odezhda/{reg}?page={id}'
    if u == 77:
        url = f'https://www.olx.ua/moda-i-stil/dlya-svadby/{reg}?page={id}'
    if u == 78:
        url = f'https://www.olx.ua/moda-i-stil/naruchnye-chasy/{reg}?page={id}'
    if u == 79:
        url = f'https://www.olx.ua/moda-i-stil/aksessuary/{reg}?page={id}'
    if u == 80:
        url = f'https://www.olx.ua/moda-i-stil/podarki/{reg}?page={id}'


    if u == 81:
        url = f'https://www.olx.ua/hobbi-otdyh-i-sport/{reg}?page={id}'
    if u == 82:
        url = f'https://www.olx.ua/zhivotnye/{reg}?page={id}'
    if u == 83:
        url = f'https://www.olx.ua/dom-i-sad/{reg}?page={id}'
    if u == 84:
        url = f'https://www.olx.ua/otdam-darom/{reg}?page={id}'
    if u == 85:
        url = f'https://www.olx.ua/rabota/{reg}?page={id}'


    print(url)

    headers = {
        "Accept": "*/*",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "no-cache",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0.0"
  }

    cookies = cookies = {'newrelic_cdn_name': 'CF'}
    html = get_html(url, headers, cookies)                    # ************************
    headers1 = html.headers
    del headers1['Content-Length']
    cookies1 = html.cookies

    soup = BeautifulSoup(html.text, 'lxml')
    #print(soup)

    # Html_file = open('oxl.html', 'w', encoding='utf-8')
    # Html_file.write(html.text)
    # Html_file.close()

    spisok = soup.find_all('div', class_='offer-wrapper')
    #print(spisok)

    i = 1
    for zapis in spisok:
        try:
           url = zapis.find('a', class_='marginright5').get('href').strip()
        except:
           url=''
        print(url)

        try:
           id = zapis.find('table' , class_='fixed').get('data-id').strip()
        except:
           id = '-'
        if i == 1:
            try:
                connection = cx_Oracle.connect('don', 'don', 'IIPS')
            except cx_Oracle.DatabaseError as e:
                code, mesg = e.args[0].message[:-1].split(': ', 1)
                try:
                    connection = cx_Oracle.connect('don', 'don', 'IIPS')
                except cx_Oracle.DatabaseError as e:
                    code, mesg = e.args[0].message[:-1].split(': ', 1)

            curs = connection.cursor()
            if id != '-':
                curs.execute(
                """
                    select id from  kosta.OLX
                          where id = :id
                """,
                id = id
                )

                data = curs.fetchall()
                if not data:
                    #print('--1--',cookies1)
                    # url = 'https://www.olx.ua/obyavlenie/prodam-videomagnitofon-IDJQHly.html?sd=1#d3c4818842'
                    html = get_html(url, headers1, cookies1) # ********************************
                    headers2 = html.headers
                    cookies2 = html.cookies

                    page = BeautifulSoup(html.text, 'lxml')

                    # print(id)


                    # Html_file = open('oxl_page.html', 'w',encoding='utf-8')
                    # # # Html_file.write(html.text)
                    # Html_file.write(str(page))
                    # Html_file.close()

                    try:
                       user_id = page.find('a', class_='quickcontact__image-link').get('href').strip()
                    except:
                       user_id=''
                    # print(user_id)

                    try:
                       saller = page.find('div', class_='offer-user__actions').find('h4').find('a').text.strip()
                    except:
                       saller=''
                    if not saller:
                        try:
                            saller = page.find('div', class_='userbox__seller-name').text.strip()
                        except:
                            saller = ''
                    if not saller:
                        try:
                            saller = page.find('h2', class_='css-owpmn2-Text').text.strip()
                        except:
                            saller = ''
                    # print(saller)

                    try:
                       title = page.find('h1').text.strip()
                    except:
                       title='-'

                    try:
                       price = page.find('strong', class_='pricelabel__value').text.strip()
                    except:
                       price=''
                    if not price:
                        try:
                            price = page.find('h3', class_='css-8kqr5l-Text').text.strip()
                        except:
                            price=''

                    try:
                       address = page.find('address').text.strip()
                       obl = page.find('address').text.split(',')[1].strip()
                    except:
                       obl = ''

                    try:
                       np = page.find('address').text.split(',')[0].strip()
                    except:
                       np=''

                    try:
                        rn = page.find('address').text.split(',')[2].strip()
                    except:
                       rn=''


                    try:
                       phone = page.find('strong', class_='xx-large').text.strip()
                    except:
                        phone =''
                    if not phone:
                        try:
                            phone = page.find('button', class_='css-atkyzk-BaseStyles').text.strip()
                        except:
                            phone = ''

                    try:
                       if phone == 'Показать телефон':
                           token = page.find('section', id='body-container').find('script')
                           token = str(token).split("'")[1]
                           ident = url.split('-ID')[1].split('.')[0]

                           url2 = f'https://www.olx.ua/ajax/misc/contact/phone/{ident}/?pt={token}'
                           del headers2['Content-Length']
                           headers2['Referer'] = url.split('#')[0]

                           if not cookies2.get('PHPSESSID'):
                               cookies2['PHPSESSID'] = cookies1.get('PHPSESSID')

                           #print('--2--' , cookies2)
                           html = get_html(url2, headers2, cookies2) # *************************************
                           phone = html.text.split('"')[3].strip().replace(' ', '').replace('(', '').replace(')', '').replace('+', '').replace('-', '')
                           if phone == '<spanclass=\\':
                               phone = html.text.split('">')[1].split('<')[0].strip().replace(' ', '').replace('(', '').replace(')', '').replace('+', '').replace('-', '')

                           if len(phone) == 10:
                               phone = '38'+phone
                           #print(html.text)
                    except:
                        phone =''

                    try:
                        if not phone:
                            phone = page.find('span', class_='spoilerHidden')
                            phone = str(phone).split('"')[5]
                            if len(phone) == 10:
                               phone = '38'+phone
                    except:
                        phone = ''

                    print(saller,phone)

                    try:
                       dat = page.find('li', class_='offer-bottombar__item').find('em').text.split(',')[1].strip()
                    except:
                       dat=''

                    try:
                        filtr1 = page.find_all('li',class_='inline')[1].find('a').text.strip()
                    except:
                        filtr1=''

                    try:
                        filtr2 = page.find_all('li',class_='inline')[2].find('a').text.strip()
                    except:
                        filtr2=''

                    try:
                        filtr3 = page.find_all('li',class_='inline')[3].find('a').text.strip()
                    except:
                        filtr3=''

                    try:
                        opis = page.find('div',class_='clr lheight20 large').text.strip()
                        opis = str(opis)[0:4000]
                    except:
                        opis=''
                    try:
                        if not opis:
                            opis = page.find('div',class_='css-g5mtbi-Text').text.strip()
                            opis = str(opis)[0:4000]
                    except:
                        opis=''

                    #print(opis)




                    curs.execute(
                    """
                        insert into kosta.olx
                            (id, title, saller, obl, np, rn, phone, price, dat, filtr1, filtr2, filtr3, opis, url, user_id)
                            values
                            (:id, :title, :saller, :obl, :np, :rn, :phone, :price, :dat, :filtr1, :filtr2, :filtr3, :opis, :url, :user_id)
                     """,
                    id = id,
                    title = title,
                    saller = saller,
                    obl = obl,
                    np = np,
                    rn = rn,
                    phone = phone,
                    price = price,
                    filtr1 = filtr1,
                    filtr2 = filtr2,
                    filtr3 = filtr3,
                    opis = opis,
                    dat = dat,
                    url = url,
                    user_id = user_id

                    )
                curs.close()
                connection.commit()
                connection.close()

def main():



    reg = ''
    reg = 'mariupol/'
    reg = 'don/'
    for u in range(1, 85):#50
        for i in range(0,25):#25
            get_data(u,i, reg)



if __name__ == '__main__':
    main()

