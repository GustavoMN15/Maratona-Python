import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from flask import Flask, render_template, request

def send_sms(info,number):
  # autenticacao twilio
  # pegue suas credenciais: http://twil.io/secure
  account_sid = ''
  auth_token = ''
  client = Client(account_sid, auth_token)
  
  client.messages.create(
    to=f'+55{number}',
    from_="number",
    body=f'{info[0]} \n {info[1]} \n {info[2]}')

def rastreio(code,number):
  url = f"https://www.linkcorreios.com.br/?id={code}"
  request = requests.get(url)
  soup = BeautifulSoup(request.text, 'html.parser')
  info = []
  cards = soup.find('ul', class_='linha_status').find_all('li')
  
  for card in cards:
    info.append(card.get_text())
  send_sms(info,number)

app = Flask('RastreadorSMS')

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/result')
def do():
  code = request.args.get('code')
  number = request.args.get('number')
  rastreio(code,number)
  return render_template('result.html', code=code)
  
app.run(host='0.0.0.0')
