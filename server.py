from flask import Flask, request, send_from_directory, Response, render_template
from compare import getSimilar
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def getIndex():
    if request.method == 'POST':
        img1 = request.form.get('img1', type=str)
        img2 = request.form.get('img2', type=str)
        return render_template('index.html', val=str(getSimilar(img1, img2)), img1=img1, img2=img2)
    else:
        return render_template('index.html', img1='http://i.imgur.com/Sbbpyvl.png', img2='http://i.imgur.com/ZcMWcXT.jpg');
        
@app.route("/main.css")
def getCss():
    return send_from_directory('css', 'main.css')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
