from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/',methods=['GET'])
def home():
	return 'You is programer sd'

def main():
	port = int(os.environ.get("PORT",5000))
	app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
	main()