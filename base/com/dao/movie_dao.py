from base import db
from base.com.vo.movie_vo import MovieVO


class MovieDAO:
    def insert_movie(self, movie_vo):
        db.session.add(movie_vo)
        db.session.commit()

    def view_movie(self):
        movie_vo_list = MovieVO.query.all()
        return movie_vo_list

    def delete_movie(self, movie_vo):
        movie_vo_list = MovieVO.query.get(movie_vo.movie_id)
        db.session.delete(movie_vo_list)
        db.session.commit()

    def edit_movie(self, movie_vo):
        movie_vo_list = MovieVO.query.filter_by(movie_id=movie_vo.movie_id).all()
        return movie_vo_list

    def update_movie(self, movie_vo):
        db.session.merge(movie_vo)
        db.session.commit()
