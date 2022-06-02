from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

users = []

print("Sorteio Instagram!")
url = input("Digite a URL de uma postagem: \n")


#setup para usar webdriver no repl.it
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#driver
driver = webdriver.Chrome(options=chrome_options)
#aqui estou deixando o tamanho do navegador (tamanho da janela)padronizado :)
# pois se a janela for muito pequena o instagram abre a versão 'mobile' ou com layout diferente. 
#Então apenas digo abaixo "Quero que o navegador seja 1024 x 768"
driver.set_window_size(1024, 768)
driver.get(url)

sleep(3)
input_username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')

input_password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
  
input_username.send_keys("email.com")
input_password.send_keys("senha")
login_button.click()
 
sleep(3)
button_info = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
button_info.click()

try:

  btn_more_comments = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button')
  while btn_more_comments.is_displayed():

    btn_more_comments.click()
    sleep(4)

    btn_more_comments = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button')
 
except Exception as err_msg:
  print(err_msg)
  pass
sleep(3)
      
comments = driver.find_elements_by_class_name('gElp9')
  
for coment in comments:
  user_name = coment.find_element_by_class_name('_6lAjh').text
  if user_name not in users:
     users.append(user_name)
  else:
    continue

print("O sorteado foi: ")
print(random.choice(users))
