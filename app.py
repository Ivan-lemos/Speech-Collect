from flask import Flask , render_template , request , jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recordings.db'
db = SQLAlchemy(app)


class Recording(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    phrase = db.Column(db.String(120) , nullable=False)
    audio_data = db.Column(db.LargeBinary , nullable=False)
    timestamp = db.Column(db.DateTime , default=datetime.utcnow)


@app.route('/')
def index():
    lang = request.args.get('lang' , 'pt')
    phrases =[]
    if lang == "en":
        phrases = ["Hello World", "Hello Word", "Hello", "World"]
    else:
        phrases = ["Olá mundo" , "Alô mundo" , "Olá mudo" , "Olá" , "mundo"]
    return render_template('index.html' , phrases=phrases , lang=lang)


@app.route('/submit' , methods=['POST'])
def submit():
    data = request.get_json()
    audio_b64 = data['audio']
    phrase = data['phrase']

    audio_bytes = base64.b64decode(audio_b64.split(',')[1])  # remove header
    new_recording = Recording(phrase=phrase , audio_data=audio_bytes)

    db.session.add(new_recording)
    db.session.commit()

    return jsonify({'status': 'success'})

@app.route("/about")
def about():
    with open("README.txt", "r", encoding="utf-8") as f:
        readme_content = f.read()
    return render_template("readme.html", content=readme_content)


@app.route("/instance/<path:filename>")
def deny_instance_access(filename):
    abort(403)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
