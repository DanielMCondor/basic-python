from ingrediente import Ingrediente

def main():
    ingrediente = Ingrediente('Papa', unidad_medida='kg')
    ingrediente.cantidad = 10
    print(ingrediente)

if __name__ == '__main__':
    main()