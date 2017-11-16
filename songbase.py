from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')


import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    #songs = db.relationship('Song', backref='artist')

@app.route('/')
def idex():
    return render_template('index.html')

@app.route('/form-demo')
def form_demo():
    return render_template('form-demo.html')


@app.route('/user/<string:name>')
def get_user(name):
    return render_template('user.html', user_name=name)

@app.route('/users')
def show_all_users():
    return '<h2> this is the page for all users </h2>'

@app.route('/artists')
def show_all_artists():
    artists = Artist.query.all()
    return render_template('artist-all.html', artists=artists)

@app.route('/songs')
def show_all_songs():
    songs = Song.query.all()
    return render_template('song-all.html', songs=songs)


if __name__ == '__main__':
    app.run()
