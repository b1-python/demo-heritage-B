
class Vivant:
    """
    Un vivant peut être vivant ou non.
    Il doit se nourir et respirer, sinon il meure.
    => Si il n'a pas respiré ou n'a pas mangé avant de vieillir, il meurt
    """

    def __init__(self):
        # Etat de l'instance
        self.vivant = True
        self.age = 0

        # Attribut pour vérifier s'il a respiré et s'est nourri
        self.nbRespiration = 0
        self.nbAlimentation = 0

    def estVivant(self):
        return self.vivant

    def getAge(self):
        return self.age

    def mourir(self):
        self.vivant = False

    def respire(self):
        if self.vivant:
            self.nbRespiration += 1
        else:
            raise ValueError

    def seNourir(self):
        if self.vivant:
            self.nbAlimentation += 1
        else:
            raise ValueError

    def vieillir(self):
        """ Fait vieillir d'un an l'animal. Il meurt s'il n'a pas respiré ou ne s'est pas nourri dans l'année """
        if self.nbRespiration == 0  or self.nbAlimentation == 0:
            # Il n'a pas respiré ou n'a pas mangé
            self.vivant = False
        else:
            self.age += 1
            self.nbRespiration = 0
            self.nbAlimentation = 0

    def __getattr__(self,attr):
        """ Cette méthode est appelé lorsqu'on tente d'accéder à un attribut/méthode qu'il n'existe pas. """
        print("appel a un attribut/méthode inexistant : "+attr)


class Animal(Vivant): # L'héritage est défini entre parenthèse => Animal hérite de Vivant

    def __init__(self):
        Vivant.__init__(self)  # dans le constructeur, il faut spécifier comment initialiser la classe mère
        self.position = 0 # attribut supplémentaire propre à un animal

    def seDeplacer(self, combien): # méthode supplémentaire qu'à un Animal et pas forcement un Vivant
        print("L'animal se déplace")
        self.position += combien

class Mamifere(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.poils = "??"

    def crier(self):
        return "..."

class Chien(Mamifere):

    def __init__(self):
        Mamifere.__init__(self)

    def crier(self):
        return "Wouaf"

class Chat(Mamifere):
    def __init__(self):
        Mamifere.__init__(self)

    def crier(self):
        return "Miaouu"
