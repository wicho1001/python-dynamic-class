import random

class Person:
    def __init__(self, name, a_paterno, age):
        self.name = name
        self.a_paterno = a_paterno
        self.age = age
        
    @property
    def sum(self):
        return self.age + 5

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

for i in range(100):
    person = Person(random.choice(nombres), random.choice(apellidos), random.choice(edades))
    persons.append(person)


def obtenerPerson(persons):
    return persons

def imprimePersonas(persons):
    print("{:30} |{:10}|{:6}|{:10}".format('Nombre', 'Apellido', 'Edad', 'Edad real'))
    print("-"*60)
    for person in persons:
        print("{:30} |{:10}|{:6}|{:9}".format(person.name, person.a_paterno, person.age, person.sum))        

def main():
    p = obtenerPerson(persons)
    imprimePersonas(p)

if __name__ == "__main__":
    main()