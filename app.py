from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello people this is MMorad the Greatest AWS Engineer!!!!!"
if __name__ == "__main__":
    app.run()
