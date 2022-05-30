from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

users = []

def do_comments(url):
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
  
  input_username.send_keys("cromeremote@gmail.com")
  input_password.send_keys("@12345a")
  login_button.click()
  
  sleep(3)
  button_info = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
  button_info.click()
  
  more_comments = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button')
  
  button =  more_comments.is_displayed()
  print(button)
  while button:
    more_comments.click()
    sleep(10)
    print(button)
    
  comments = driver.find_elements_by_class_name('gElp9')
  for coment in comments:
    user_name = coment.find_element_by_class_name('_6lAjh').text
    if user_name not in users:
       users.append(user_name)
    else:
      print()


    
print(users)