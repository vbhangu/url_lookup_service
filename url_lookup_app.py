from flask import (Flask, render_template, request)
from URLLookupSvc import URLLookupSvc

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('home.html')


@app.route("/verify", methods=['GET'])
def verify():
    data = request.args.get('url')
    response = URLLookupSvc.if_found(URLLookupSvc(data).get_domain(), URLLookupSvc.view_db())
    return response


if __name__ == "__main__":
    app.run(debug=True)
