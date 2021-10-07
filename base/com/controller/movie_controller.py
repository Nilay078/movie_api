from flask import render_template, request, redirect

from base import app
from base.com.dao.movie_dao import MovieDAO
from base.com.vo.movie_vo import MovieVO


@app.route('/', methods=['POST', 'GET'])
def movie_home():
    try:
        return render_template('add_movie.html')
    except Exception as ex:
        print("<<<<<<<<<<<<<movie_home route exception occured>>>>>>>>>>", ex)


@app.route('/home', methods=['POST', 'GET'])
def default_movie_home():
    try:
        return render_template('add_movie.html')
    except Exception as ex:
        print("<<<<<<<<<<<<<default_movie_home route exception occured>>>>>>>>>>", ex)


@app.route('/insert_movie', methods=['POST'])
def add_movie():
    try:
        movie_name = request.form.get('Name')
        movie_timing = request.form.get('Timing')
        movie_location = request.form.get('Location')

        movie_vo = MovieVO()
        movie_dao = MovieDAO()

        movie_vo.movie_name = movie_name
        movie_vo.movie_timing = movie_timing
        movie_vo.movie_location = movie_location
        movie_dao.insert_movie(movie_vo)

        return redirect('/view_movie')
    except Exception as ex:
        print("<<<<<<<<<<<<<add_movie route exception occured>>>>>>>>>>", ex)


@app.route('/view_movie')
def view_movie():
    try:
        movie_dao = MovieDAO()
        movie_vo_list = movie_dao.view_movie()
        return render_template('view_movie.html', movie_vo_list=movie_vo_list)
    except Exception as ex:
        print("<<<<<<<<<<<<<view_movie route exception occured>>>>>>>>>>", ex)


@app.route('/delete_movie', methods=['GET'])
def delete_movie():
    try:
        movie_dao = MovieDAO()
        movie_vo = MovieVO()

        movie_vo.movie_id = request.args.get('movieId')
        movie_dao.delete_movie(movie_vo)
        return redirect('/view_movie')

    except Exception as ex:
        print("<<<<<<<<<<<<<<<<<delete_movie route exception occured>>>>>>>>>>", ex)


@app.route('/edit_movie', methods=['GET'])
def edit_movie():
    try:
        movie_vo = MovieVO()
        movie_dao = MovieDAO()

        movie_id = request.args.get('movieId')
        print("<<<<<<<<<movie_id>>>>>", movie_id)
        movie_vo.movie_id = movie_id
        movie_vo_list = movie_dao.edit_movie(movie_vo)
        return render_template('edit_movie.html', movie_vo_list=movie_vo_list)
    except Exception as ex:
        print("<<<<<<<<<<<<<<<<<<<edit_movie route exception occured>>>>>>>>>>", ex)


@app.route('/update_movie', methods=['POST'])
def update_movie():
    try:
        movie_id = request.form.get('movieId')
        movie_name = request.form.get('Name')
        movie_timing = request.form.get('Timing')
        movie_location = request.form.get('Location')

        movie_vo = MovieVO()
        movie_dao = MovieDAO()

        print("------------------", movie_id, movie_name, movie_timing, movie_location)

        movie_vo.movie_id = movie_id
        movie_vo.movie_name = movie_name
        movie_vo.movie_timing = movie_timing
        movie_vo.movie_location = movie_location
        movie_dao.update_movie(movie_vo)
        print(movie_id, movie_name, movie_timing, movie_location)
        return redirect('/view_movie')
    except Exception as ex:
        print("<<<<<<<<<<<<<<<<<<<<<<update_movie route exception occured>>>>>>>>>>", ex)
