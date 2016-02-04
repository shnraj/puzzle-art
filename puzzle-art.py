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
              '9': '----.', ' ': '  '}


@app.route('/')
def main_form():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def main_form_post():
    text = request.form['text']
    return morse(text)


@app.route('/morse/<msg>')
def morse(msg):
    morse = ''
    for char in msg:
        morse += MORSE_CODE[char.upper()] + ' '
    return render_template('puzzle-art.html', msg=msg, morse_msg=morse.strip())


if __name__ == "__main__":
    app.run(debug=True)
