from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "HHello World this is Morad the best AWS Engineer!!!!!"
if __name__ == "__main__":
    app.run()
