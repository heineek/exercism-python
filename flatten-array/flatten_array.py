def flatten(inputs):
    def is_with_nested(input_list):
        for item in input_list:
            if type(item) is list:
                return True
        return False

    while is_with_nested(inputs):
        for pos, item in enumerate(inputs):
            if type(item) is list:
                inputs.pop(pos)
                ins_pos = pos
                for i in range (0, len(item)):
                    inputs.insert(ins_pos, item[i])
                    ins_pos += 1
                break

    result = [input for input in inputs if type(input) is int or type(input) is str]

    return result