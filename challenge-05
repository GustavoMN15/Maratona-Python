import requests
import os
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"
countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code = items[2].text
  if code != "":
    country = {
    'name': name,
    'code': code
    }
    countries.append(country)
    
def menu():
  for index, country in enumerate(countries):
    print(f"{index} -> {country['name']}")
  
  print("Bem-vindo!")
  print("Escolha o pais para consultar a moeda\n")
  try:
    choice = int(input())
    if choice > len(countries):
      print("nao tem, escolha um item da lista")
      menu()
    else:
      country = countries[choice]
      print(f"Pais: {country['name']} \nMoeda: {country['code']}")
      restart()
  except:
    print("Voce tem que digitar um numero!")

def restart():
    option = input("Deseja escolher mais algum pais? S/n\n").lower()
    
    if option == "s":
      os.system('clear')
      menu()
      
    elif option == "n":
      print("Programa finalizado")
    else:
      print("Opção invalida!")
      restart()
      
menu()

# já deixei instalado e importado o requests
# e o BeautifulSoup.
# a variavel com a url do iban tbm ;) 

## LEIA AS DICAS DE OURO 

# pode apagar esses comentários após ler

# BOM DESAFIO!
