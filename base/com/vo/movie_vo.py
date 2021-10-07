from base import db


class MovieVO(db.Model):
    __tablename__ = 'movie_table'
    movie_id = db.Column('movie_id', db.Integer, primary_key=True, autoincrement=True)
    movie_name = db.Column('movie_name', db.String(255), nullable=False)
    movie_timing = db.Column('movie_timing', db.String(255), nullable=False)
    movie_location = db.Column('movie_location', db.String(255), nullable=False)

    def as_dict(self):
        return {
            'movie_id': self.movie_id,
            'movie_name': self.movie_name,
            'movie_timing': self.movie_timing,
            'movie_location': self.movie_location,
        }


db.create_all()
