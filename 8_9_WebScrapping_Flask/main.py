import requests
from flask import Flask, render_template, request

app = Flask('MaratonaScrapping')

@app.route('/')
def home():
  url = 'https://hn.algolia.com/api/v1/search?tags=story'
  url_popular = requests.get(url).json()
  url_p = url_popular.get('hits')
  return render_template('index.html', list=url_p)

@app.route('/recent')
def recent():
  url = 'https://hn.algolia.com/api/v1/search_by_date?tags=story'
  url_recent = requests.get(url).json()
  url_p = url_recent.get('hits')
  return render_template('recent.html', lista=url_p)

@app.route('/<id>')
def id(id):
  r = f'http://hn.algolia.com/api/v1/items/{id}'
  url = requests.get(r).json()
  return render_template('id.html', comments=url)

app.run(host='0.0.0.0')