import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///music.db"

db = SQLAlchemy(app)


class Features(db.Model):
    __tablename__ = 'features'

    id = db.Column(db.String(64), primary_key=True)
    popularity = db.Column(db.Float)
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    loudness = db.Column(db.Float)
    speechiness = db.Column(db.Float)
    duration_ms = db.Column(db.Float)
    tempo = db.Column(db.Float)

    def __repr__(self):
        return '<Features %r>' % (self.name)


class Map(db.Model):
    __tablename__ = 'map'

    country_code = db.Column(db.String(64), primary_key=True)
    market_count = db.Column(db.Float)

    def __repr__(self):
        return '<Map %r>' % (self.name)


class Genre(db.Model):
    __tablename__ = 'genre'

    genre = db.Column(db.String(64), primary_key=True)
    count = db.Column(db.Float)

    def __repr__(self):
        return '<Genre %r>' % (self.name)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("recommend.html")
    # return "hi"


<<<<<<< HEAD
@app.route("/predict")
def predict(song):
=======
@app.route("/search/<song>")
def searchRoute(song):
    print(song)
    # Fetch song name, artist name, and album via API call
    # songInfo = search(song)
    songInfo = search(song)
    return jsonify(songInfo)


@app.route("/recommend", methods=['POST'])
def recommend():
>>>>>>> origin/Evan

    # Fetch song features via API call

    # Load trained model

    # User song features to make a model.predict
    # What kind of database setup is required?

    #

    # data = list of top 5 songs

    # """Return all features"""

    results = db.session.query(Features.id, Features.popularity, Features.danceability, Features.energy,
                               Features.loudness, Features.speechiness, Features.duration_ms, Features.tempo).all()

    song_id = [result[0] for result in results]
    popularity = [result[1] for result in results]
    danceability = [result[2] for result in results]
    energy = [result[3] for result in results]
    loudness = [result[4] for result in results]
    speechiness = [result[5] for result in results]
    duration_ms = [result[6] for result in results]
    tempo = [result[7] for result in results]

    # # Format the data to send as json
    # data = [{
    #     "song_id": song_id,
    #     "popularity": popularity,
    #     "danceability": danceability,
    #     "energy": energy,
    #     "loudness": loudness,
    #     "speechiness": speechiness,
    #     "duration_ms": duration_ms,
    #     "tempo": tempo
    # }]
    # check return for html ID
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
