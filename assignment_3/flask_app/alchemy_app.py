from flask import Flask, request, render_template
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
import ner

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dc6e4e24fb5113780f8b15f0efb9bc6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nlp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    dependency = db.Column(db.Text)
    head = db.Column(db.Text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        text = request.form['text']
        doc = ner.SpacyDocument(text)
        ents = doc.get_dependency()
        for e in ents:
            ent = Entity(text = e[0], dependency = e[1], head = e[2])
            db.session.add(ent)
        db.session.commit()
        ents= Entity.query.group_by('text')
        return render_template('new_result.html', ents=ents)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(host = '0.0.0.0', debug=True)