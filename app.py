from flask import Flask, render_template
import data
app = Flask(__name__)

city = {'ekb':'Из Екатеринбурга','msk':'Из Москвы','spb':'Из Петербурга','kazan':'Из Казани','nsk':'Из Новосибирска'}

@app.route("/")
def start_index(): 
    dic={}
    i=0
    for k,v in data.tours.items():
        if i == 6:
            break
        i+=1
        dic[k]=v
    return render_template('index.html',d=dic)

@app.route('/departures/') 
def start_depart():
    return render_template('departure.html')

@app.route('/departures/<departure>/') 
def post_depart(departure):
    S = []
    n = []
    for k,v in data.tours.items():
        if v["departure"]==departure:
            S.append(int(v["price"]))
            n.append(int(v["nights"]))
    S.sort()
    n.sort()
    if len(S) in [1,21]:
        t='тур'
    elif len(S) in [2,3,4]:
        t='тура'
    else:
        t = 'туров'
    return render_template('departure.html',d=data.tours,dep=departure,kol=len(S),min_n=n[0],max_n=n[-1],min_S=S[0],max_S=S[-1],gorod=city[departure],text=t)

@app.route('/tours/') 
def start_tour():
    return render_template('tour.html')

@app.route('/tours/<id>/') 
def post_tour(id):
    id=int(id)
    d=data.tours[id]
    return render_template('tour.html',title=d['title'],country=d['country'],dep=city[d['departure']],n=d['nights'],desc=d['description'],sum=d['price'],picture=d['picture'])

#@app.errorhandler(404)
#def render_not_found(error):
#    return "Что-то не так, но мы все починим:\n{}".format(error), 404

#@app.errorhandler(500)
#def render_server_error(error):
#    return "Что-то не так, но мы все починим"


app.run(debug=True) 