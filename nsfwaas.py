from flask import Flask, request
import nsfwnet

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return "Working..."

@app.route("/nsfw", methods=["POST"])
def classify():
    global nsfw
    fsImage =  request.files.get("image")
    if fsImage:
        return "%f" % nsfwnet.nsfwnet.classify(fsImage.read())
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0")
