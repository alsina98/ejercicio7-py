class Alumno:
    nombre = ''
    nota = 0
    def nombre(self, valor):
        self.nombre = valor
    def nota(self, valor):
        if valor >= 6:
            self.nota = valor
        else:
            self.nota = valor

nombre = input("Escribe tu nombre")
nota = int(input("¿Cual es tu nota?"))

a = Alumno()
a.nombre(nombre)
a.nota(nota)

print("Alumno",a.nombre)

match a.nota:
    case 1:
        print("Nota:",a.nota,"Suspendido")
    case 2:
        print("Nota:",a.nota,"Suspendido")
    case 3:
        print("Nota:",a.nota,"Suspendido")
    case 4:
        print("Nota:",a.nota,"Suspendido")
    case 5:
        print("Nota:",a.nota,"Suspendido")
    case 6:
        print("Nota:",a.nota,"Aprobado")
    case 7:
        print("Nota:",a.nota,"Aprobado")
    case 8:
        print("Nota:",a.nota,"Aprobado")
    case 9:
        print("Nota:",a.nota,"Aprobado")
    case 10:
        print("Nota:",a.nota,"Aprobado")