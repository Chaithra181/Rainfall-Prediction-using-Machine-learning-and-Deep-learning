from flask import Flask,request,render_template,redirect
import main

app = Flask(__name__)




@app.route('/', methods =['GET','POST'])
def login():
    if (request.method == 'POST'):
        username = request.form['name']
        password = request.form['password']
        if(username == 'user'):
            if(password == '11111'):
                return redirect('/home')
    return render_template('login.html')

@app.route('/login1')
def login1():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/state', methods=['GET', 'POST'])
def state():
    return render_template('state.html')

@app.route('/graph', methods=['GET', 'POST'])
def graph():
    if (request.method == 'POST'):
        statename = request.form['state']
        years = int(request.form['year'])
        prediction = main.stateLinearPredict(statename, years)
        print(prediction)
        return render_template('graph.html', temp=prediction, state=statename)

@app.route('/statedl', methods=['GET', 'POST'])
def statedl():
    return render_template('statedl.html')

@app.route('/graph2', methods=['GET', 'POST'])
def graph2():
    if (request.method == 'POST'):
        statename = request.form['state']
        years = int(request.form['year'])
        prediction = main.stateCNNPredict(statename, years)
        print(prediction)
        return render_template('graphdl.html', temp=prediction, state=statename)

@app.route('/districts', methods=['GET', 'POST'])
def districts():
    return render_template('districts.html')

@app.route('/graphdistrict', methods=['GET','POST'])
def graphdistrict():
    if(request.method == 'POST'):
        districtname = request.form['district']
        state = request.form['state']
        prediction = main.districtpredict(districtname, state)
        print(prediction)
        return render_template('graph1.html',temp=prediction, district=districtname)

@app.route('/districtsdl', methods=['GET', 'POST'])
def districtsdl():
    return render_template('districtsdl.html')

@app.route('/graphdistrict2', methods=['GET','POST'])
def graphdistrict2():
    if (request.method == 'POST'):
        districtname = request.form['district']
        state = request.form['state']
        prediction = main.districtpredict(districtname, state)
        print(prediction)
        return render_template('graphdl1.html', temp=prediction, district=districtname)




if __name__ == "__main__":
    app.run(debug=True)