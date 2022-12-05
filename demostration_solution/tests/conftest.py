from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    
    d1 = Director(id=1, name='TestName')
    d2 = Director(id=2, name='TestName2')
    d3 = Director(id=3, name='TestName3')
    d4 = Director(id=4, name='TestName4')
    
    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    director_dao.create = MagicMock(return_value=d4)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()
    
    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    
    g1 = Genre(id=1, name='TestName')
    g2 = Genre(id=2, name='TestName2')
    g3 = Genre(id=3, name='TestName3')
    g4 = Genre(id=4, name='TestName4')
    
    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])
    genre_dao.create = MagicMock(return_value=g4)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()
    
    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    
    m1 = Movie(id=1, title='TestTitle', description="Тестовое описание", year=2000)
    m2 = Movie(id=2, title='TestTitle2', description="Тестовое описание2")
    m3 = Movie(id=3, title='TestTitle3', year=2003)
    m4 = Movie(id=4, title='TestTitle4', genre_id=1, trailer="http://ya.ru")
    
    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.create = MagicMock(return_value=m4)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
    
    return movie_dao
