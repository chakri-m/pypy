from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello World this is Moradd the best AWS Engineer!!!!!"
if __name__ == "__main__":
    app.run()