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


if __name__ == "__main__":
    app.run(debug=True)
