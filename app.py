from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloworld():
    return "Hello coucou Worlgerd tfhis is MMorad the best AWS Engineer!!!!!"
if __name__ == "__main__":
    app.run()
