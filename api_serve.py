#parte 1
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os


#parte 2
url_target = "http://www.adorocinema.com/filmes/melhores/"


#parte 3

app = Flask(__name__)


#parte 4
@app.route('/',methods=['GET'])
def home():
	return 'You is programer'




#parte 5
@app.route('/api/filmes', methods=['GET'])

def filmes():
	html_doc = urlopen(url_target)
	soup = BeautifulSoup(html_doc,"html.parser")

	data = []

	for dataBox in soup.find_all('div',class_='card entity-card entity-card-list cf'):
		titleObg = dataBox.find('h2',class_='meta-title').find('a',class_='meta-title-link').text
		durationObj = dataBox.find('div',class_='meta-body-item meta-body-info')
		img_cont = soup.find('img',class_='thumbnail-img')['src'] 
			
		data.append({
			'title':titleObg.strip(),
			'img_src':img_cont.strip()
			})

	return jsonify({'filmes': data})	

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
 