from typing import List

import pytest

from .task import task4


class Case:
    def __init__(self, name: str, data: str,
                 reqs: List[List], answer: List[int]):
        self._name = name
        self.reqs = reqs
        self.data = data
        self.answer = answer

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        data='bcbdbcb',
        reqs=[[2, 1, 4],
              [1, 4, 'c'],
              [1, 5, 'c'],
              [2, 4, 6],
              [2, 1, 7]],
        answer=[3, 1, 2]
    ),
    Case(
        name='base2',
        data='egdccdgfffecbfb',
        reqs=[[1, 6, 'f'],
              [1, 4, 'c'],
              [2, 6, 14],
              [1, 7, 'c'],
              [1, 12, 'd'],
              [2, 6, 8],
              [2, 1, 6],
              [1, 7, 'd'],
              [1, 2, 'g'],
              [1, 10, 'b'],
              [2, 7, 9],
              [1, 10, 'b'],
              [1, 14, 'c'],
              [1, 1, 'g'],
              [2, 1, 11]],
        answer=[5, 2, 5, 2, 6]
    ),
    Case(
        name='base3',
        data='egdccddccgfffcddccgfffecbfbbcbdbcbecbfbbcbdbcbdccdccgfbcbdbccddccgfffecbfbbcbdbcbbffecbfbdcbcbdbcbc',
        reqs=[[1, 6, 'f'],
              [1, 4, 'c'],
              [2, 6, 14],
              [1, 7, 'c'],
              [1, 12, 'd'],
              [2, 6, 8],
              [2, 1, 6],
              [1, 7, 'd'],
              [1, 2, 'g'],
              [1, 10, 'b'],
              [2, 7, 9],
              [1, 10, 'b'],
              [1, 14, 'c'],
              [1, 1, 'g'],
              [2, 1, 11],
              [2, 20, 8],
              [2, 60, 6],
              [1, 70, 'd'],
              [1, 2, 'g'],
              [1, 90, 'b'],
              [40, 70, 9],
              [1, 10, 'b'],
              [1, 14, 'c'],
              [1, 1, 'g']],
        answer=[4, 2, 5, 2, 5, 2, 2, 2]
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    answer = task4(
        data=case.data,
        reqs=case.reqs
    )
    assert answer == case.answer
