from flask import Flask, render_template
import urllib, json


app = Flask(__name__)

@app.route("/")
def hello():
    data=json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=YOURAPIKEYHERE&limit=1").read())
    print(json.dumps(data, sort_keys=True, indent=4))
    giphys = json.dumps(data, sort_keys=True, indent=4)

    return render_template('index.html', giphys=giphys)

if __name__ == "__main__":
    app.run(debug=True)
