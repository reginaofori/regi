import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template

application = Flask(__name__)
random.seed()  # Initialize the random number generator


@application.route('/')
def index():
    return render_template('chart.html')


@application.route('/chart-data')
def chart_data():
    def generate_random_data():
        timing = 0
        while True:
            number = random.randint(56, 79)
            timing += 1
            json_data = json.dumps(
                {'time': str(timing) + 'sec' , 'value': number})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
