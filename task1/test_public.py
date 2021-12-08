from typing import List

import pytest

from .task import task1


class Case:
    def __init__(self, name: str,
                 start: int, end: int,
                 edges: List[List[int]], answer: List[int]):
        self._name = name
        self.start = start
        self.end = end
        self.edges = edges
        self.answer = answer

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        start=1,
        end=4,
        edges=[[1, 2, 1],
               [1, 3, 4],
               [1, 4, 5],
               [2, 3, 1],
               [2, 4, 4],
               [3, 4, 1]],
        answer=[1, 2, 3, 4]
    ),
    Case(
        name='base2',
        start=1,
        end=10,
        edges=[[1, 5, 12],
               [2, 4, 140],
               [2, 10, 149],
               [3, 6, 154],
               [3, 7, 9],
               [3, 8, 226],
               [3, 10, 132],
               [4, 10, 55],
               [5, 8, 33],
               [7, 8, 173]],
        answer=[1, 5, 8, 7, 3, 10]
    ),
    Case(
        name='base3',
        start=2,
        end=4,
        edges=[[1, 2, 1],
               [1, 3, 4],
               [1, 4, 5],
               [2, 3, 1],
               [2, 4, 4],
               [3, 4, 1]],
        answer=[2, 3, 4]
    ),
    Case(
        name='base4',
        start=3,
        end=10,
        edges=[[1, 4, 201],
               [2, 3, 238],
               [3, 4, 40],
               [3, 6, 231],
               [3, 8, 45],
               [4, 5, 227],
               [4, 6, 58],
               [4, 9, 55],
               [5, 7, 14],
               [6, 10, 242]],
        answer=[3, 4, 6, 10]
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = task1(
        start=case.start,
        end=case.end,
        edges=case.edges
    )
    assert answer == case.answer
