import abc
from typing import Callable, List

from freneticlib.representations import abstract_representation


class AbstractMutationOperator(abc.ABC):
    @abc.abstractmethod
    def __call__(self, representation: abstract_representation.RoadRepresentation, test):
        pass

    def __str__(self):
        return self.__class__.__name__

    def is_applicable(self, test) -> bool:
        return True


class AbstractMutator(abc.ABC):
    def __init__(self, operators: List[Callable]):
        self.operators = operators

    def get_all(self) -> List[Callable]:
        return self.operators
