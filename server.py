from flask import Flask, request, jsonify
from web_calculator import calculate_next_state
import configparser

'''
Create an instance of Flask class - a web application framework written in Python.
The first argument is the name of the application's module or package.
We are using a single module, so we use __name__.
'''
app = Flask(__name__)

try:
    # create a configparser.
    config = configparser.ConfigParser()
    config.read('server_conf.ini')
    # initialize socket parameters.
    app_ip = config['APP_INFO']['ip']
    app_port = int(config['APP_INFO']['port'])
except Exception as e:
    print('Error in initialization', e)

'''
calculate function is mapped to the '/calculate' URL.
'''
@app.route('/calculate', methods=['POST'])
def calculate():
    # extract the state.
    calculator_state = None
    if 'calculatorState' in request.json:
        calculator_state = request.json['calculatorState']
    input = request.json['input']
    return jsonify(calculate_next_state(calculator_state, input))

'''
main function of the program.
'''
if __name__ == '__main__':
    try:
        # to run on specific ip and port use : app.run(host='IP', port=X).
        app.run(host=app_ip, port=app_port)
    except Exception as e:
        print('Error occurred', e)
