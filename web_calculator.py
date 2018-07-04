import re, json

number = re.compile('[0-9]')
operator = re.compile('[\+\-\*\/\=]')

def calculate_next_state(json_state, input):
    if not json_state:
        json_state = {}
        json_state['num1'] = json_state['num2'] = json_state['operator'] = json_state['display'] = ''

    #json_state = json.loads(json_state)
    if number.match(input):
        if not json_state['operator']:
            # operator is null.
            json_state['num1'] = json_state['num1'] + input
            json_state['display'] = json_state['num1']
        else:
            # operator isn't null.
            if json_state['operator'] == '=' and not json_state['num2']:
                # clear data.
                json_state['num1'] = input
                json_state['display'] = input
                json_state['operator'] = ''
            else:
                json_state['num2'] = json_state['num2'] + input
                json_state['display'] = json_state['num2']
    elif operator.match(input):
        if (not json_state['operator'] and json_state['num1']) or (json_state['operator'] and not json_state['num2']):
            # operator is null.
            json_state['operator'] = input
        elif json_state['num1'] and json_state['num2']:
            op = json_state['operator']
            if op == '+':
                json_state['display'] = str(int(json_state['num1']) + int(json_state['num2']))
            elif op == '-':
                json_state['display'] = str(int(json_state['num1']) - int(json_state['num2']))
            elif op == '*':
                json_state['display'] = str(int(json_state['num1']) * int(json_state['num2']))
            elif op == '/':
                json_state['display'] = str(int(json_state['num1']) / int(json_state['num2']))

            json_state['num1'] = json_state['display']
            json_state['operator'] = input
            json_state['num2'] = ''
    return json_state
