from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def start_index():
    return render_template('index.html')

@app.route('/departures/') 
def start_depart():
    return render_template('departure.html')

@app.route('/departures/<departure>/') 
def post_depart(departure):
    return "Departure #" + departure

@app.route('/tours/') 
def start_tour():
    return render_template('tour.html')

@app.route('/tours/<id>/') 
def post_tour(id):
    return "Tour #" + id

#@app.errorhandler(404)
#def render_not_found(error):
#    return "Что-то не так, но мы все починим:\n{}".format(error), 404

#@app.errorhandler(500)
#def render_server_error(error):
#    return "Что-то не так, но мы все починим"


app.run(debug=True) 