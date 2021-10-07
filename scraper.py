import requests
import time
from bs4 import BeautifulSoup as bs
import csv

URL = "http://books.toscrape.com/catalogue"
LAPAS = "lapas/"
DATI = "dati/"

def saglabat(url, datne):
    rezultats = requests.get(url)
    if rezultats.status_code == 200:
        with open(f"{LAPAS}{datne}", 'w', encoding='UTF-8') as f:
            f.write(rezultats.text)
    else:
        print(f"ERROR: Statusa kods {rezultats.status_code}")


def lejupieladet_lapas(cik):
    for i in range(1, cik + 1):
        saglabat(f"{URL}/page-{i}.html", f"{i}_lapa.html")
        time.sleep(1)

def info(datne):
    dati = []
    with open(datne, 'r', encoding='UTF-8') as f:
        html = f.read()

    base = bs(html, "html.parser")

    galvena = base.find_all("article", class_="product_pod")
    
    #tabulas = galvena.find_all("article")
    print(galvena)
    # for i in range(1, len(galvena)):
    #     print("==========================")
    #     print(galvena[i].get_text())
    print("==========================")
    #auto_tabula = tabulas[1]

    # rindas = auto_tabula.find_all("tr")

    # for rinda in rindas[1:-1]:
    #     auto = {}
    #     # print(rinda)
    #     # print("=======================")
    #     # print("=======================")
    #     # print("=======================")    

info("lapas/1_lapa.html")

#lejupieladet_lapas(5)