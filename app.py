from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "1Helllok World this is mmgMora the jbest AWS Engineer!!!!!"
if __name__ == "__main__":
    app.run()
