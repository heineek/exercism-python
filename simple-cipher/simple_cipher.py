import random


class Cipher(object):
    def __init__(self, key=''):
        if key:
            self.key = key
        else:
            key_list = [chr(random.randint(97, 122)) for _ in range(101)]
            self.key = ''.join(key_list)
        for char in self.key:
            if not char.isalpha() or not char.islower():
                raise ValueError
        self.shift_list = [ord(char) - ord('a') for char in self.key]

    def encode(self, msg):
        result = []

        key_passes = len(msg) // len(self.key)
        chars_left = len(msg) % len(self.key)

        shift = []

        for _ in range(key_passes):
            shift.extend(self.shift_list)

        for i in range(chars_left):
            shift.append(self.shift_list[i])

        for pos, char in enumerate(msg):
            result.append(chr(ord(char) + shift[pos]))

        return ''.join(result)

    def decode(self, msg):
        result = []

        key_passes = len(msg) // len(self.key)
        chars_left = len(msg) % len(self.key)

        shift = self.shift_list.copy()

        for _ in range(key_passes):
            shift.extend(self.shift_list)

        for i in range(chars_left + 1):
            shift.append(self.shift_list[i])

        for pos, char in enumerate(msg):
            result.append(chr(ord(char) - shift[pos]))

        return ''.join(result)


class Caesar(object):
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.mapped_alphabet = self.alphabet[3:] + self.alphabet[:3]
        self.encode_map = {self.alphabet[i]: self.mapped_alphabet[i] for i in range(len(self.alphabet))}
        self.decode_map = {self.mapped_alphabet[i]: self.alphabet[i] for i in range(len(self.mapped_alphabet))}

    def encode(self, msg):
        msg_encoded = [self.encode_map[char.lower()] for char in msg if char.isalpha()]
        return ''.join(msg_encoded)

    def decode(self, msg):
        msg_decoded = [self.decode_map[char] for char in msg]
        return ''.join(msg_decoded)