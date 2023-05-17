from flask_classic import app

@app.route("/")
def index ():
    return "Proyecto final"