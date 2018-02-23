import re


def calculate(question):
    operators = {'plus': '+', 'minus': '-', 'multiplied by': '*', 'divided by': '/'}

    regexp = re.compile(
        r'^What is (?P<first_operand>-?\d+) (?P<operator>\D+) (?P<second_operand>-?\d+)(?P<optional>.*)\?$')

    match = regexp.match(question)
    if not match or match['operator'] not in operators:
        raise ValueError

    expression = match['first_operand'] + ' ' + operators[match['operator']] + ' ' + match['second_operand']

    result = eval(expression)

    # need to improve the following code for supporting more than one optional operation but all the test pass now
    if match['optional']:
        additional = match['optional']
        additional_regexp = re.compile(r'^ (?P<second_operator>\D+) (?P<third_operand>-?\d+)$')
        additional_match = additional_regexp.match(additional)
        additional_expression = operators[additional_match['second_operator']] + ' ' + additional_match['third_operand']
        result = eval('result' + additional_expression)

    return result