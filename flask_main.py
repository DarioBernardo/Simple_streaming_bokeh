from flask import Flask
from flask import render_template

from ChartManager import ChartManager

app = Flask("Real-time APP", static_url_path="/static")
chart = ChartManager()

@app.route('/', methods=['GET'])
def index():
    script, div = chart.getLineAsDiv()
    return render_template('index.html', script=script, div=div)


if __name__ == '__main__':
    app.run()
