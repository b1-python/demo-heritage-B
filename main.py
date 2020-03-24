from vivants import Vivant, Animal, Chien, Chat


vivant1 = Animal()
# Affichage de l'instance (en pratique on n'accède pas directement aux attributs mais on utilise les méthodes)
print("vivant1:")
print(vivant1.age)
print(vivant1.vivant)

vivant2 = Vivant()
print("vivant2:")
print(vivant2.age)
print(vivant2.vivant)

# 1ère année
vivant1.seNourir()
vivant2.seNourir()
vivant1.respire()
vivant2.respire()

vivant1.vieillir()
vivant2.vieillir()

print(" ---- Après un an ----")
print("vivant1:")
print(vivant1.age)
print(vivant1.vivant)
print("vivant2:")
print(vivant2.age)
print(vivant2.vivant)

# 2ère année
vivant1.seNourir()
vivant1.respire()
vivant2.respire()

vivant1.vieillir()
vivant2.vieillir()
print(" ---- Après deux an ----")
print("vivant1:")
print(vivant1.age)
print(vivant1.vivant)
print("vivant2:")
print(vivant2.age)
print(vivant2.vivant)

# 3ème année
print("---- 3ème année ----")
vivant3 = Vivant()
vivant1.seNourir()
vivant1.respire()
vivant1.seDeplacer(10) # vivant1 étant un animal, il peut se déplacer
#vivant3.seDeplacer(5) # impossible => la classe Vivant ne contient pas de méthode seDeplacer
print(vivant3)


print(" ---- Les chiens et chats ----")

snoopy = Chien()
jerry = Chat()

print(snoopy.crier())
print(jerry.crier())

print("Le chenil:")
chenil = []
chenil.append(Chat())
chenil.append(Chien())
chenil.append(Chien())
chenil.append(Chat())
for mamifere in chenil:
    print(mamifere.crier())

