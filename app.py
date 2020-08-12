import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open('ipl_score_pred.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods =['POST'])
def predict():
    var_store = []
    
    if request.method == 'POST':
        batting_team = request.form['batting_team']
        if batting_team == 'Chennai Super Kings':
            var_store = var_store + [0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            var_store = var_store + [1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            var_store = var_store + [0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            var_store = var_store + [0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            var_store = var_store + [0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            var_store = var_store + [0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            var_store = var_store + [0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            var_store = var_store + [0,0,0,0,0,0,1]
        
        bowling_team = request.form['bowling_team']
        if bowling_team == 'Chennai Super Kings':
            var_store = var_store + [0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            var_store = var_store + [1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            var_store = var_store + [0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            var_store = var_store + [0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            var_store = var_store + [0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            var_store = var_store + [0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            var_store = var_store + [0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            var_store = var_store + [0,0,0,0,0,0,1]
    
        venue = request.form['venue']
        if venue == 'Feroz Shah Kotla':
            var_store = var_store + [1,0,0,0,0,0,0,0]
        elif venue == 'M Chinnaswamy Stadium':
            var_store = var_store + [0,1,0,0,0,0,0,0]
        elif venue == 'MA Chidambaram Stadium, Chepauk':
            var_store = var_store + [0,0,1,0,0,0,0,0]
        elif venue == 'Punjab Cricket Association Stadium, Mohali':
            var_store = var_store + [0,0,0,1,0,0,0,0]
        elif venue == 'Rajiv Gandhi International Stadium, Uppal':
            var_store = var_store + [0,0,0,0,1,0,0,0]
        elif venue == 'Sawai Mansingh Stadium':
            var_store = var_store + [0,0,0,0,0,1,0,0]
        elif venue == 'Wankhede Stadium':
            var_store = var_store + [0,0,0,0,0,0,1,0]
        elif venue == 'other':
            var_store = var_store + [0,0,0,0,0,0,0,1]
        elif venue == 'Eden Gardens':
            var_store = var_store + [0,0,0,0,0,0,0,0]
        
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        overs = float(request.form['overs'])
        runs_last_5 = int(request.form['runs_last_5'])
        wickets_last_5 = int(request.form['wickets_last_5'])
        
        var_store = var_store + [runs,wickets,overs,runs_last_5,wickets_last_5]
        
        data = np.reshape(var_store,(1,27))
        pred = int(model.predict(data)[0])

        return render_template('index1.html', lower_limit = pred - 7, upper_limit = pred + 8)   


if __name__ == '__main__':
	app.run(debug=True)     