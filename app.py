from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "HHello World this is Raphael the best cyber security coach!!!!!"
if __name__ == "__main__":
    app.run()
