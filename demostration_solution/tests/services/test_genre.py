import pytest

from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None

    def test_get_all(self):
        genre = self.genre_service.get_all()
        assert len(genre) > 1

    def test_create(self):
        data = {
            'name': 'TestName4'
        }
        genre = self.genre_service.create(data)
        assert genre.id is not None

    def test_update(self):
        self.genre_service.update(1)

    def test_delete(self):
        res = self.genre_service.delete(1)
        assert res is None