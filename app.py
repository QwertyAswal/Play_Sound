from playsound import playsound
from flask import Flask

app = Flask(__name__)


@app.route('/play_sound',methods=['GET','POST'])
def play_sound():
    playsound("sample.mp3")
    return "success"


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
