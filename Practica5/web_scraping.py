from bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://www.espn.com.mx/futbol/posiciones/_/liga/uefa.champions")

soup = BeautifulSoup(url.content, "html.parser")
resultado = soup.find("tbody", {"class":"Table__TBODY"})
equipos = resultado.text
lista = [1,2,3,4]
for i in lista:
    x = str(i)
    lista = list(equipos.split(x))
#print(lista + "\n")

x = open("archivo.txt", "w")
for i in lista:
    x.write(i + "\n")
x.close()
