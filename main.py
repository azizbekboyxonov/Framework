from wsgiref.simple_server import make_server
from app import Frameworkapp

app = Frameworkapp()

@app.route("/muhammadyusuf")
def muhammadyusuf(request, response):
    response.text = "yoshi: 16, yili: 2008"

from flask import Flask, send_file, abort

app = Flask(__name__)

@app.route("/home")
def home():
    text = "<h2>Hi you are in the home page!</h2>"
    return text

@app.route("/about")
def about():
    text2 = "<h2>This page is localhost page for waitress theme!</h2>"
    return text2

@app.route("/sardor")
def sardor():
    img_tag = '<img src="/sardor/image" alt="Sardor rasmi" width="300"><br>'

    info = """
        <h2>Melikulov Sardor</h2>
        <p>
            <span style="font-size: 18px;">Age: 16 da</span><br>
            <span style="font-size: 18px;">Hobby: Football</span><br>
            <span style="font-size: 18px;">Main task: Studying at school</span><br>
            <span style="font-size: 18px;">Zodiac sign: Unknown</span><br>
        </p>
        """
    return img_tag + info

@app.route("/sardor/image")
def sardor_image():
    try:
        image_path = r"C:\Users\Asus\Desktop\sardor.jpg"
        return send_file(image_path, mimetype="image/jpeg")
    except FileNotFoundError:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
