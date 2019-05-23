import random

class Person:
    def __init__(self, name, a_paterno, age):
        self.name = name
        self.a_paterno = a_paterno
        self.age = age

    def __str__(self):
        return "{:30} |{:10}|{:6}|{:9}".format(self.name, self.a_paterno, self.age, self.sum)    

    @property
    def sum(self):
        return self.age + 5

class Alumno(Person):
    def __init__(self, name, a_paterno, age, matricula):
        super().__init__(name, a_paterno, age)
        self.matricula = matricula
    def __str__(self):
        return "{:30} |{:10}|{:6}|{:9}| {}".format(self.name, self.a_paterno, self.age, self.sum, self.matricula)    
    
    

apellidos = [
"Abad",
"Abalos",
"Abarca",
"Abendano",
"Abila",
"Abina",
"Abitua",
"Aboites",
"Abonce",
"Abrego",
"Abrica",
"Abrigo",
"Abundis",
"Aburto",
"Acebedo",
"Acebes" 
]

nombres = [
"Egidia",
"Eginia",
"Elbira",
"Elena",
"Eleuteria",
"Elias",
"Eligia",
"Elijia",
"Eliza",
"Elizabeth",
"Ella",
"Ellena",
"Elodia",
"Elogia",
"Eluteria",
"Elvira"
]

edades = list(range(15, 100))

persons = []
alumnos = []

for i in range(50):
    person = Person(random.choice(nombres), random.choice(apellidos), random.choice(edades))
    persons.append(person)

for i in range(50):
    m = random.choices(edades, k=3)
    m = "".join(str(m).split(','))
    alumno = Alumno(random.choice(nombres), 
            random.choice(apellidos), 
            random.choice(edades),
            m 
            )
    alumnos.append(alumno)


def obtenerPerson(persons):
    return persons

def obtenerAlumnos(alumnos):
    return alumnos

print("{:30} |{:10}|{:6}|{:10}|{:10}".format('Nombre', 'Apellido', 'Edad', 'Edad real', 'Matricula'))
def imprime(lista):
    print("-"*60)
    for i in lista:
        print(i)        

def main():
    p = obtenerPerson(persons)
    a = obtenerAlumnos(alumnos)
    imprime(p)
    imprime(a)

if __name__ == "__main__":
    main()