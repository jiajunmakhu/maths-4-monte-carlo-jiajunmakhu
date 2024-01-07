
class LCG:
    def __init__(self, initial_seed: int, a: int, c: int, m: int):
        self.seed = initial_seed
        self.a = a
        self.c = c
        self.m = m

    def next(self) -> float:
        """
        Volgende stap van de rng. Gebruikt de vorige berekende waarde van dit algoritme om de volgende te berekenen.
        Het resultaat wordt gedeeld door de m, zodat deze een waarde tussen de 0 en 1 wordt.
        :return:
        Returnt de nieuwe waarde tussen 0 en 1.
        """
        self.seed = self.cong(self.seed)
        return self.seed/self.m

    def cong(self, seed: int) -> float:
        """
        Zet de formule voor de Linear Congruential Generator om in code.
        De formule is X_n = (a * X_n-1 + c) mod m. Hierin zijn a, c en m positieve nummers, maar a en c moeten kleiner
        dan m zijn. a kan ook geen 0 zijn, terwijl c dat wel kan. X_n-1 is de vorige berekende waarde
        :param seed: The previous calculated value using LCG or the first given seed
        :return:
        Returnt de nieuwe waarde
        """
        return (self.a * seed + self.c) % self.m


class LFG:
    def __init__(self, initial_seed: int, j: int, k: int, m: int, operator):
        self.j = j
        self.k = k
        self.m = m
        self.initial_seed = initial_seed
        self.operator = operator
        # Deze lijst houdt de berekende waarden bij
        self.calculated_values = self.create_calculated_values_list(self.initial_seed, self.k)

    def next(self) -> float:
        """
        Zet de formule voor Lagged Fibonacci Generator om in code.
        De formule is X_n = (X_n-j $ X_n-k) mod m, waarin de j en de k het aantal iteraties terug is van de berekende
        waarde. Bijvoorbeeld uit lijst [n1,n2,n3,n4] = [12,23,43,45] waarbij de meest linker index de oudste berekende
        waarde is, geeft j = 2 de waarde 43, aangezien de nieuwe waarde de n5 wordt en 2 stappen terug is n5 - 2 = n3.
        :return:
        Returnt de nieuwe waarde
        """
        new_value = self.operator(self.calculated_values[-self.j], self.calculated_values[-self.k]) % self.m
        self.calculated_values.append(new_value)
        self.calculated_values.pop(0)
        return new_value/self.m

    @staticmethod
    def create_calculated_values_list(initial_seed: int, k: int):
        """
        Deze functie creert een lijst van een lengte k die random getallen geeft.
        :param initial_seed: De begin seed voor het genereren van de willekeurige getal
        :param k: Lengte van de lijst
        :return:
        Lijst van lengte k
        """
        lcg = LCG(initial_seed, 214013, 2531011, 2**32)
        calculated_values = []
        for _ in range(0, k):
            # Waarde van nieuwe getal keer de m geeft weer een getal ipv een percentage
            calculated_values.append(int(lcg.next() * 2**32))
        return calculated_values

