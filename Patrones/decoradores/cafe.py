from abc import ABC, abstractmethod

class Cafe(ABC):
    def __init__(self) -> None:
        self._descripcion = 'Cualquier café'

    def set_descripcion(self, valor: str) -> str:
        self._descripcion = valor

    def get_descripcion(self):
        return self._descripcion

    @abstractmethod
    def calcular_costo(self) -> float:
        raise NotImplementedError

class Frappuccino(Cafe):
    def __init__(self) -> None:
        self._descripcion = 'Frappuccino'

    def calcular_costo(self) -> float:
        return 1.99

class Latte(Cafe):
    def __init__(self):
        self._descripcion = 'Latte'

    def calcular_costo(self) -> float:
        return 1.85
