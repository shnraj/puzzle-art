from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              ' ': '  ', '.': '.-.-.-', ',': '--..--',
              ':': '---...', '?': '..--..', '\'': '.----.',
              '-': '-....-', '/': '-..-.', '(': '-.--.-',
              ')': '-.--.-', '"': '.-..-.', '@': '.--.-.',
              '=': '-...-', '!': '-.-.--', '+': '.-.-.',
              '_': '..--.-', '&': '.-...', ';': '-.-.-.'}

ALPHABET = {'A': 1,    'B': 2,   'C': 3,
            'D': 4,    'E': 5,   'F': 6,
            'G': 7,    'H': 8,   'I': 9,
            'J': 10,   'K': 11,  'L': 12,
            'M': 13,   'N': 14,  'O': 15,
            'P': 16,   'Q': 17,  'R': 18,
            'S': 19,   'T': 20,  'U': 21,
            'V': 22,   'W': 23,  'X': 24,
            'Y': 25,   'Z': 26,  ' ': 0}

BARCODE = {'A': [2, 1, 1, 0, 1, 2], 'B': [1, 2, 1, 0, 1, 2],
           'C': [2, 2, 1, 0, 1, 1], 'D': [1, 1, 2, 0, 1, 2],
           'E': [2, 1, 2, 0, 1, 1], 'F': [1, 2, 2, 0, 1, 1],
           'G': [1, 1, 1, 0, 2, 2], 'H': [2, 1, 1, 0, 2, 1],
           'I': [1, 2, 1, 0, 2, 1], 'J': [1, 1, 2, 0, 2, 1],
           'K': [2, 1, 1, 1, 0, 2], 'L': [1, 2, 1, 1, 0, 2],
           'M': [2, 2, 1, 1, 0, 1], 'N': [1, 1, 2, 1, 0, 2],
           'O': [2, 1, 2, 1, 0, 1], 'P': [1, 2, 2, 1, 0, 1],
           'Q': [1, 1, 1, 2, 0, 2], 'R': [2, 1, 1, 2, 0, 1],
           'S': [1, 2, 1, 2, 0, 1], 'T': [1, 1, 2, 2, 0, 1],
           'U': [2, 0, 1, 1, 1, 2], 'V': [1, 0, 2, 1, 1, 2],
           'W': [2, 0, 2, 1, 1, 1], 'X': [1, 0, 1, 2, 1, 2],
           'Y': [2, 0, 1, 2, 1, 1], 'Z': [1, 0, 2, 2, 1, 1],

           '0': [1, 1, 0, 2, 2, 1], '1': [2, 1, 0, 1, 1, 2],
           '2': [1, 2, 0, 1, 1, 2], '3': [2, 2, 0, 1, 1, 1],
           '4': [1, 1, 0, 2, 1, 2], '5': [2, 1, 0, 2, 1, 1],
           '6': [1, 2, 0, 2, 1, 1], '7': [1, 1, 0, 1, 2, 2],
           '8': [2, 1, 0, 1, 2, 1], '9': [1, 2, 0, 1, 2, 1],

           ' ': [1, 0, 2, 1, 2, 1], '.': [2, 0, 1, 1, 2, 1],
           '-': [1, 0, 1, 1, 2, 2]}


@app.route('/')
def main_form():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def main_form_post():
    if request.form['submit'] == 'Go Morse':
        morse_text = request.form['morse_text']
        return morse(morse_text)
    if request.form['submit'] == 'Go Alphabet':
        alphabet_text = request.form['alphabet_text']
        return alphabet(alphabet_text)
    if request.form['submit'] == 'Go Barcode':
        barcode_text = request.form['barcode_text']
        return barcode(barcode_text)


@app.route('/morse/<msg>')
def morse(msg):
    morse = ''
    for char in msg:
        morse += MORSE_CODE.get(char.upper(), char) + ' '

    morse_arr = []
    for char in morse.strip():
        if char == '.':
            morse_arr.append(0)
        elif char == '-':
            morse_arr.append(1)
        elif char == ' ':
            morse_arr.append(2)
    return render_template('puzzle-art.html', msg=msg.strip(),
                           puzzle_msg=morse.strip(), arr=morse_arr)


@app.route('/alphabet/<msg>')
def alphabet(msg):
    alphabet_nums = []
    for char in msg:
        alphabet_nums.append(ALPHABET.get(char.upper(), char))

    return render_template('puzzle-art.html', msg=msg.strip(),
                           puzzle_msg=' '.join(str(e) for e in alphabet_nums),
                           arr=alphabet_nums)


@app.route('/barcode/<msg>')
def barcode(msg):
    barcode_nums = []
    for char in msg:
        barcode_nums.extend(BARCODE.get(char.upper(), char))

    return render_template('puzzle-art.html', msg=msg.strip(),
                           puzzle_msg=' '.join(str(e) for e in barcode_nums),
                           arr=barcode_nums)


if __name__ == "__main__":
    app.run(debug=True)
