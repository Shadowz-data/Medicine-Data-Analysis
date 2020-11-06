import pandas as pd
import flask
from flask import Flask, request, render_template

app = flask.Flask(__name__, template_folder='templates')

data = pd.read_csv("Final Medicine Result.csv")

all_condition = sorted(set(data["condition"]))

@app.route('/', methods=['GET', 'POST'])


def assist():
    
    if flask.request.method == 'GET':
        return(flask.render_template('home.html', all_condition = all_condition))

    if request.method == 'POST':
    	condition = request.form['condition']
    	con = condition
    	result = data[data['condition'] == condition]
    	final = result.nlargest(10,['rating','positive'])

    return render_template('home.html', all_condition = all_condition, tables=[final.to_html(index=False)])


if __name__ == '__main__':
    app.run(debug=True)    	
