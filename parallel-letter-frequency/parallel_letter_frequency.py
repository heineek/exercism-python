from concurrent.futures import ThreadPoolExecutor, as_completed


def calculate(text_input):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    results = {}

    with ThreadPoolExecutor(max_workers=26) as executor:
        text = ''.join(text_input)
        future_count = [executor.submit(count, letter, text) for letter in alphabet]

        for f in as_completed(future_count):
            ltr, num = f.result()
            if num != 0:
                results[ltr] = num

    return results


def count(letter, text):
    result = 0
    for char in text:
        if char.isalpha() and char.lower() == letter:
            result += 1

    return letter, result