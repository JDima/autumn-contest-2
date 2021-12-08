from typing import List

import pytest

from .task import task3


class Case:
    def __init__(self, name: str,
                 Q: int, N: int,
                 events: List[List[int]], answer: List[int]):
        self._name = name
        self.Q = Q
        self.N = N
        self.events = events
        self.answer = answer

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        N=3,
        Q=4,
        events=[[1, 3],
                [1, 1],
                [1, 2],
                [2, 3]],
        answer=[1, 2, 3, 2]
    ),
    Case(
        name='base2',
        N=4,
        Q=6,
        events=[[1, 2],
                [1, 4],
                [1, 2],
                [3, 3],
                [1, 3],
                [1, 3]],
        answer=[1, 2, 3, 0, 1, 2]
    ),
    Case(
        name='base3',
        N=10,
        Q=85,
        events=[[2, 2], [1, 10], [1, 1], [2, 6], [1, 2], [1, 4], [1, 7], [2, 1], [1, 1], [3, 3], [1, 9], [1, 6], [1, 8],
                [1, 10], [3, 8], [2, 8], [1, 6], [1, 3], [1, 9], [1, 6], [1, 3], [1, 8], [1, 1], [1, 6], [1, 10],
                [2, 1], [2, 10], [1, 10], [1, 1], [1, 10], [1, 6], [1, 2], [1, 8], [1, 3], [1, 4], [1, 9], [1, 5],
                [1, 5], [2, 2], [2, 4], [1, 7], [1, 1], [2, 4], [1, 9], [1, 1], [1, 7], [1, 8], [3, 33], [1, 10],
                [2, 2], [1, 3], [1, 10], [1, 6], [3, 32], [2, 3], [1, 5], [2, 10], [2, 2], [2, 4], [2, 3], [3, 16],
                [1, 3], [2, 2], [1, 1], [3, 18], [2, 2], [2, 5], [1, 5], [1, 9], [2, 4], [1, 3], [1, 4], [1, 3], [1, 6],
                [1, 10], [2, 2], [1, 7], [1, 7], [2, 8], [1, 1], [3, 1], [1, 8], [1, 10], [1, 7], [1, 8]],
        answer=[0, 1, 2, 2, 3, 4, 5, 4, 5, 3, 4, 5, 6, 7, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18, 17, 16, 17, 18, 18, 19, 20, 21, 22, 3, 4, 4, 5, 6, 7, 7, 6, 7, 5, 5, 5, 5, 5, 6, 6,
                7, 7, 7, 6, 7, 8, 8, 9, 10, 11, 12, 13, 13, 14, 15, 14, 15, 15, 16, 17, 18, 19]
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = task3(
        N=case.N,
        Q=case.Q,
        events=case.events
    )
    assert answer == case.answer
