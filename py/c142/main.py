from flask import Flask, jsonify
import csv

from storage import all_movies, liked_movies, not_liked_movies, did_not_watch
from demographic_filtering import output
from content_filtering import get_recommendations


app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    movie_data = {
        "title": all_movies[0][18],
        "poster_link": all_movies[0][26],
        "release_date": all_movies[0][12] or "N/A",
        "duration": all_movies[0][14],
        "rating": all_movies[0][19],
        "overview": all_movies[0][8]
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    # Signifies that we are modifying the global variable here, as we tend to modify it inside a function.
    global all_movies
    movie = all_movies[0]
    # all_movies = all_movies[1:]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }), 201

# As we post each movie as liked or not liked, the next movie appears in GET request get_movie
@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    global all_movies
    movie = all_movies[0]
    # all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }), 201
    # 201 is success message for POST, 200 is for GET

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch_view():
    global all_movies
    movie = all_movies[0]
    did_not_watch.append(movie)
    did_not_watch.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-movies")
def popular_movies():
    movie_data = []
    # output refers to the output from get_recommendations file.
    for movie in output:
        # Single Pre Underscore is used for internal use. Most of us don't use it because of that reason.
        # https://www.datacamp.com/community/tutorials/role-underscore-python
        _d = {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date": movie[2] or "N/A",
            "duration": movie[3],
            "rating": movie[4],
            "overview": movie[5]
        }
        movie_data.append(_d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    }), 200

@app.route("/recommended-movies")
def recommended_movies():
    all_recommended = []
    for liked_movie in liked_movies:
        output = get_recommendations(liked_movie[18])
        for data in output:
            all_recommended.append(data)
    # We cant keep recommending the same movie again and again..so to remove duplicates,use itertools.groupby
    import itertools
    all_recommended.sort()
    # _ can be used as a variable in looping.. It is a special character in python used for various purposes.
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    print(all_recommended[0])
    movie_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "poster_link": recommended[1],
            "release_date": recommended[2] or "N/A",
            "duration": recommended[3],
            "rating": recommended[4],
            "overview": recommended[5]
        }
        movie_data.append(_d)
    return jsonify({
        "data": movie_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()