import requests
import os

print('Bem vindo ao verificador de sites 1.0!')

def input_url():
  list = input("Insira as URLs dos sites que deseja verificar o status   separados por virgula!\n").lower().split(",")
  do_test(list)

def do_test(list):
  
  for url in list:
    url = url.strip()

    if "." not in url:
      print(f'{url} URL invalida!')
      
    else:
      if "http" not in url:
        url = f'http://{url}'
      try:
        r = requests.get(url)
        if r.status_code == 200:
          print(f'{url} site OK!')
        else:
          print(f'{url} site offline!')
          
      except:
        print(f'{url} site offline!')
  restart()
        

def restart():
  option = input("Deseja testar mais sites? S/n\n").lower()
  
  if option == "s":
    os.system('clear')
    input_url()
    
  elif option == "n":
    print("Programa finalizado")
  else:
    print("Opção invalida!")
    input_url()



input_url()

## Já deixei instalado o package do Requests e também importado aqui para você. Está pronto para usar.
## E não se esquece de pesquisar sobre try: e except: para tratar erros do Request. (isso pode te ajudar)

## pode apagar esses comentários haha.

 
## Bom desafio!
