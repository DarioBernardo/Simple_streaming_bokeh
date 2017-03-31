from flask import Flask, jsonify
from flask import make_response
from flask import render_template

from ChartManager import ChartManager

app = Flask("Real-time APP", static_url_path="/static")
chart = ChartManager()

@app.route('/', methods=['GET'])
def index():
    script, div = chart.getLineAsDiv()
    return render_template('index.html', script=script, div=div)

@app.route('/new_point', methods=['GET'])
def new_point():
    x = chart.get_new_data_point()
    y = chart.get_new_data_point()
    return make_response(jsonify({'x':x, 'y':y}), 200)


if __name__ == '__main__':
    app.run()
