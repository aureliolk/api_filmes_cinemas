from flask import Flask, jsonify, request, render_template, redirect
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from flask import Flask
from flask_cors import CORS
import os
import time

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
url_target = "http://www.adorocinema.com/filmes/melhores/"

@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')

# @app.before_request
# def before_request():
#     if request.url.startswith('http://'):
#         url = request.url.replace('http://', 'https://', 1)
#         code = 301
#         return redirect(url, code=code)

@app.route('/api/filmes', methods=['GET'])
def filmes():
	html_doc = urlopen(url_target)
	soup = BeautifulSoup(html_doc,"html.parser")
	data = []
	for dataBox in soup.find_all('li',class_='mdl'):
		titleObg = dataBox.find('h2', class_='meta-title').find('a',class_='meta-title-link')
		img_cont = dataBox.find('img', class_='thumbnail-img')
		if(img_cont['src'] == 'data:image/gif;base64,R0lGODlhAwAEAIAAAAAAAAAAACH5BAEAAAAALAAAAAADAAQAAAIDhI9WADs='):
			imgSrc = img_cont['data-src']
		else:
			imgSrc = img_cont['src']
		data.append({
		'title':titleObg.text.strip(),
		'img_src':imgSrc
		})
	return jsonify({'filmes': data})
def main():	
	port = int(os.environ.get("PORT",5000))
	app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
	main()