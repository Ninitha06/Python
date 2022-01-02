from flask import Flask, jsonify
import csv

all_movies = []
# If we dont specify encoding, it throws UnicodeDecodeError for the file we downloaded from colab.
with open('movies.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch_movies = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    # Signifies that we are modifying the global variable here, as we tend to modify it inside a function.
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

# As we post each movie as liked or not liked, the next movie appears in GET request get_movie
@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201
    # 201 is success message for POST, 200 is for GET

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()