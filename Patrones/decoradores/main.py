from cafe import Cafe, Latte, Frappuccino
from decoradores import CremaBatida, Leche, Helado, Caramelo

def ver_detalle(cafe: Cafe) -> None:
    print(f'{cafe.get_descripcion()} cuesta {cafe.calcular_costo()}')

if __name__ == '__main__':
    cafe01 = Frappuccino()
    cafe01 = Helado(Leche(Helado(CremaBatida(cafe01))))
    ver_detalle(cafe01)