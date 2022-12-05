from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director


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

