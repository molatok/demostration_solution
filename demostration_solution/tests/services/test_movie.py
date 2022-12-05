import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert isinstance(movie.id, int)
        assert movie.title == "TestTitle"

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 1

    def test_create(self):
        data = {
            'name': 'TestTitle4'
        }
        movie = self.movie_service.create(data)
        assert movie.id is not None
        assert movie.title == 'TestTitle4'

    def test_update(self):
        self.movie_service.update(1)

    def test_delete(self):
        res = self.movie_service.delete(1)
        assert res is None