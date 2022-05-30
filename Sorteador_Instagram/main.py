from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from driver import do_comments

print("Sorteio Instagram!")
url = input("Digite a URL de uma postagem: \n")
if "." not in url:
  print(f'{url} URL invalida!')  
else:
  do_comments(url)