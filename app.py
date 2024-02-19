from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "2Hgelllok Worlgerd tfhis is mmgkMora th jlmbest AWS Engineer!!!!!"
if __name__ == "__main__":
    app.run()
