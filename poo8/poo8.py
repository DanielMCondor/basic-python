from pelicula import Pelicula

def main():
    peliculas = []
    peliculas.append(Pelicula('El padrino', 'francis Ford Coppola', 1972, 175))
    peliculas.append(Pelicula('Sueño de fuga', 'Frank Darabont', 1994, 142))
    peliculas.append(Pelicula('La lista de schindler', 'Steven Spielberg', 1993, 195))
    peliculas.append(Pelicula('Toro salvaje', 'Martin Scorsese', 1980, 129))
    peliculas.append(Pelicula('Casablanca', 'Michael Curtiz', 1942, 102))
    peliculas.append(Pelicula('Casablanca', 'Michael Curtiz', 1942, 102))

    peliculas.sort()
    # print('igual igual: ',peliculas[0] == peliculas[1])
    # print('menor igual: ',peliculas[0] <= peliculas[1])
    # print('-'*30)
    for pelicula in peliculas:
        print(pelicula)
        print('-'*30)

    print(f'Menor pelicula en la coleccion: \n {min(peliculas)}')
    print(f'Mayor pelicula en la coleccion: \n {max(peliculas)}')

if __name__ == '__main__':
    main()