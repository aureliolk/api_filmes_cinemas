from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
url_target = "http://www.adorocinema.com/filmes/melhores/"

@app.route('/',methods=['GET'])
def home():
	return 'You is programer sd'

@app.route('/api/filmes', methods=['GET'])
def filmes():
	html_doc = urlopen(url_target)
	soup = BeautifulSoup(html_doc,"html.parser")

	data = []

	for dataBox in soup.find_all('div',class_='card entity-card entity-card-list cf'):
		titleObg = dataBox.find('h2', class_='meta-title').find('a',class_='meta-title-link')
		img_cont = dataBox.find('img', class_='thumbnail-img')['src']
		data.append({
		'title':titleObg.text.strip(),
		'img_src':img_cont.strip()
		})
	return jsonify({'filmes': data})	

def main():
	port = int(os.environ.get("PORT",5000))
	app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
	main()