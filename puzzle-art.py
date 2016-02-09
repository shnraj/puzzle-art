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
        morse += MORSE_CODE.get(char.upper(), char) + ' '

    msg_arr = []
    for char in morse.strip():
        if char == '.':
            msg_arr.append(0)
        elif char == '-':
            msg_arr.append(1)
        elif char == ' ':
            msg_arr.append(2)
    return render_template('puzzle-art.html', msg=msg.strip(),
                           morse_msg=morse.strip(), arr=msg_arr)


if __name__ == "__main__":
    app.run(debug=True)
