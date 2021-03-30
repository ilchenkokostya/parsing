import re
import csv
import requests
from bs4 import BeautifulSoup
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"D:\app\kot\product\instantclient_19_8")


def write_csv(data):
    with open('result.csv', 'a', newline='') as f:
        fields = ['t0', 't1', 't2', 't3', 't4', 't5']
        writer = csv.DictWriter(f, fieldnames=fields, delimiter=';')
        writer.writerow(data, )


def get_html(url, headers):
    response = requests.get(url, headers=headers)
    if not response.ok:  # .status_code == 200:
        print(f'Code: {response.status_code}, url: {url}')
    return response


def get_data(id):
    # url = f'http://mariupol.ukrgo.com/view_subsection.php?id_subsection=146&&page={id}'
    url = f'http://donetsk.ukrgo.com/view_subsection.php?id_subsection=146&page={id}'
    # url = f'http://kramatorsk.ukrgo.com/view_subsection.php?id_subsection=146&page={id}'
    # url = f'http://slavyansk.ukrgo.com/view_subsection.php?id_subsection=146&page={id}'

    # url = f'http://volnovakha.ukrgo.com/view_subsection.php?id_subsection=146&page={id}'
    #url = f'http://gorlovka.ukrgo.com/view_subsection.php?id_subsection=146&page={id}'



    headers = {

        "Accept": "text / html, application / xhtml + xml, application / xml;    q = 0.9, image / webp, * / *;q = 0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",

    }
    html = get_html(url, headers)
    soup = BeautifulSoup(html.text, 'lxml')

    spisok = soup.find('div', class_='main-content').find_all('h3')

    i = 1
    for zapis in spisok:
        if i == 1:
            try:
                html = get_html(zapis.find('a').get('href').strip(), headers)
                page = BeautifulSoup(html.text, 'lxml')
                # page = BeautifulSoup('http: // mariupol.ukrgo.com / post_19067196_krasavicy_hotjat_intima.html', 'lxml')

                title = page.find_all('tr')

                try:
                    titl = title[12].td.h1.text.strip()
                except:
                    titl = '-'

                try:
                    dat = title[13].td.div.text.strip().split('\n')[0]
                    dat = dat.split(': ')[1]
                except:
                    dat = '-'

                try:
                    gorod = title[13].td.div.text.strip().split('\n')[1]
                    gorod = gorod.split(': ')[1]
                except:
                    gorod = '-'

                try:
                    t1 = title[13].td.div.text.strip().split('\n')[2]
                except:
                    t1 = '-'
                try:
                    t2 = title[14].td.div.text.strip().split('  ')[0]
                except:
                    t2 = '-'

                # print( id, dat, zapis.find('a').get('href').strip())

                connection = cx_Oracle.connect('don', 'don', 'IIPS')
                curs = connection.cursor()

                '''Нажимаем кнопку показать'''
                if page.find(id="post-phones-show-div") != None:
                    phone = page.find(id="post-phones-show-div").find('input').get('onclick').split("'")
                    params = {
                        'i': phone[1],
                        's': phone[3]
                    }
                    cookies = html.cookies
                    cookies.update({'b': 'b'})
                    html = requests.post('http://mariupol.ukrgo.com/moduls/showphonesnumbers.php', data=params,
                                         headers=headers, cookies=cookies)
                    phone = BeautifulSoup(html.text, 'lxml')
                    t4 = phone.find('span').text.strip()

                    # data = {
                    #     't0': zapis.find('a').get('href').split("_")[1],
                    #     't1': t1,
                    #     't2': t2,
                    #     't3': t3,
                    #     't4': "'"+t4,
                    #     't5': zapis.find('a').get('href').strip()
                    # }
                    # write_csv(data)


                    curs.execute(
                        """
                                select id from  kosta.ukrgo
                                          where id = :id 
                        """,
                        id=zapis.find('a').get('href').split("_")[1]
                    )

                    data = curs.fetchall()

                    if not data:
                        print(t4,url,zapis.find('a').get('href').strip())
                        curs.execute(
                            """
                                    insert into kosta.ukrgo 
                                           (id, titl, dat, gorod, text1, text2, phone, url)
                                           values 
                                           (:id, :titl, :dat, :gorod, :text1, :text2, :phone, :url)
                            """,
                            id=zapis.find('a').get('href').split("_")[1],
                            titl=titl,
                            dat=dat,
                            gorod=gorod,
                            text1=t1,
                            text2=t2,
                            phone=t4,
                            url=zapis.find('a').get('href').strip()
                        )
                    curs.close()
                    connection.commit()
                    connection.close()


            except:
                pass

    # print(zapis.find('a').get('href').split("_")[1] + "------------")


def main():
    for i in range(0, 100):
        get_data(i)


if __name__ == '__main__':
    main()
