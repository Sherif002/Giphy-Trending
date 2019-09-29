from flask import Flask, render_template
import urllib, json
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config())

@app.route("/<limit>")
def index(limit):
    data=json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/trending?api_key=" + app.config['GIPHY_API_KEY'] + "&limit=" + limit).read())
    giphys = [i['images']['original']['url'] for i in data['data']]
    return render_template('index.html', giphys=giphys)

if __name__ == "__main__":
    app.run(debug=True)
