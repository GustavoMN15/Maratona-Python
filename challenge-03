def add_food(food=None, food_desc=None):
  if food == None or food_desc == None:
    print("Voce precisa digitar a comida e a descrição!")
  elif type(food) != str or type(food_desc) != str:
    print("Voce precisa digitar valores string!")
  else:
    if food in food_list:
      print("A comida ja existe!")
    else:
      food_list [food] = food_desc 
      print("Comida Adicionada")
      print(food_list)

def delete_food(food=None):
  if food == None:
    print("Voce precisa digitar a comida!")
  elif type(food) != str:
    print("Voce precisa digitar valores string!")
  else:
    if food in food_list:
      del food_list[food]
      print('Comida removida!')
    else:
      print("A comida nao existe!")

def update_food(food=None, food_desc=None):
  if food == None or food_desc == None:
    print("Voce precisa digitar a comida e a descrição!")
  elif type(food) != str or type(food_desc) != str:
    print("Voce precisa digitar valores string!")
  else:
    if food not in food_list:
      print("Comida não existente!")
    else:
      food_list.update({food: food_desc})    
      print("Adicionado com sucesso!")

def get_food(food=None):
  if food == None:
     print("Voce precisa digitar a comida!")
  elif type(food) != str:
    print("Voce precisa digitar valores string!")
  else:
    if food not in food_list:
      print("Comida não existente!")
    else:
      print(food_list.get(food))
      
# use esta parte de cima para declarar a 4 funções #


#####################################################
#####!! NÃO EDITE O CÓDIGO ABAIXO DESTA LINHA !!#####

#criação da food_list
food_list = {
  'paçoquinha': 'Um doce de amendoím brasileiro',
  'brigadeiro': 'Um doce muito delicioso',
  'pizza': 'um tipo de comida da italia',
  'hamburguer': 'comida dos USA'
}

#####################################
######## TESTES ADD_FOOD #########
#####################################

# ADD_FOOD - TESTE 1
print("\n#### ADD_FOOD - TESTE 1")
print("Usando add_food com valores sendo int")
print("add_food(100, 23)\n")
#excuta:
add_food(100, 23)

# ADD_FOOD - TESTE 2
print("\n#### ADD_FOOD - TESTE 2")
print("Usando add_food sem passar a descrição.")
print("add_food('pizza')\n")
#excuta:
add_food('pizza')

# ADD_FOOD - TESTE 3
print("\n#### ADD_FOOD - TESTE 3")
print("Usando add_food com comida já existente.")
print("add_food('brigadeiro', 'Um doce brasileiro')\n")
#excuta:
add_food('brigadeiro', 'Um doce brasileiro')

# ADD_FOOD - TESTE 4
print("\n#### ADD_FOOD - TESTE 4")
print("Usando add_food adicionando uma comida.")
print("add_food('lasanha', 'Camadas de massa e molho')\n")
#excuta:
add_food('lasanha', 'Camadas de massa e molho')


#####################################
######## TESTES DELETE_FOOD #########
#####################################

# DELETE_FOOD - TESTE 1
print("\n#### DELETE_FOOD - TESTE 1")
print("Usando delete_food com valor sendo int")
print("delete_food(100)\n")
#excuta:
delete_food(100)

# DELETE_FOOD - TESTE 2
print("\n#### DELETE_FOOD - TESTE 2")
print("Usando delete_food sem nenhum valor.")
print("delete_food()\n")
#excuta:
delete_food()

# DELETE_FOOD - TESTE 3
print("\n#### DELETE_FOOD - TESTE 3")
print("Usando delete_food com comida que não existe na lista.")
print("delete_food('massa')\n")
#excuta:
delete_food('massa')

# DELETE_FOOD - TESTE 4
print("\n#### DELETE_FOOD - TESTE 4")
print("Usando delete_food removendo uma comida.")
print("delete_food('paçoquinha')\n")
#excuta:
delete_food('paçoquinha')

#####################################
## TESTES UPDATE_FOOD ##
#####################################

# UPDATE_FOOD - TESTE 1
print("\n#### UPDATE_FOOD - TESTE 1")
print("Usando update_food com valores sendo int")
print("update_food(100, 23)\n")
#excuta:
update_food(100, 23)

# UPDATE_FOOD - TESTE 2
print("\n#### UPDATE_FOOD - TESTE 2")
print("Usando update_food sem passar a descrição.")
print("update_food('pizza')\n")
#excuta:
update_food('pizza')

# UPDATE_FOOD - TESTE 3
print("\n#### UPDATE_FOOD - TESTE 3")
print("Usando update_food com comida não existente.")
print("update_food('sorvete', 'Um doce gelado da italia')\n")
#excuta:
update_food('sorvete', 'Um doce gelado da italia')


# UPDATE_FOOD - TESTE 4
print("\n#### UPDATE_FOOD - TESTE 4")
print("Usando update_food e atualizando uma comida.")
print("update_food('brigadeiro', 'Melhor doce do mundo.')\n")
#excuta:
update_food('brigadeiro', 'Melhor doce do mundo.')

#####################################
## TESTES GET_FOOD ##
#####################################

# GET_FOOD - TESTE 1
print("\n#### GET_FOOD - TESTE 1")
print("Usando get_food com valor sendo int")
print("get_food(505)\n")
#excuta:
get_food(505)

# GET_FOOD - TESTE 2
print("\n#### GET_FOOD - TESTE 2")
print("Usando get_food sem passar a comida.")
print("get_food()\n")

get_food()

# GET_FOOD - TESTE 3
print("\n#### GET_FOOD - TESTE 3")
print("Usando get_food com comida não existente.")
print("get_food('noodle')\n")
get_food('noodle')

# GET_FOOD - TESTE 4
print("\n#### GET_FOOD - TESTE 4")
print("Usando get_food e pesquisando a descrição uma comida.")
print("get_food('hamburguer')\n")
get_food('hamburguer')


#####!!!!!!!!!!!!!! THE END !!!!!!!!!!!!!!#####


## Linha de Chegada ##
print("\n Winners win")
print(u"\U0001F40D" + " Maratona Python")
# © 2022 Maratona Python. Todos os direitos reservados.
# https://brunofraga.com
