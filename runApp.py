from flask import *
import pub, sub

app = Flask(__name__)


@app.route("/")
def HomePage():
    pub.handler()   # uruchomienie mqtt na localhost  -> wysyła w pętli komunikat z randomowym intem z zakresu 50-100
    # data = pub.handler()
    # return "Hello world! " + str(data)


if __name__ == "__main__":
    app.run(debug=True)
