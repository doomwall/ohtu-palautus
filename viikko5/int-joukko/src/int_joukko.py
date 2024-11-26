KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = self._luo_lista(kapasiteetti)
        self.alkioiden_lkm = 0

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        found = False

        for i in self.lukujono:
            if i == n:
                found = True

        if found:
            return True
        
        return False

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return

        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm == len(self.lukujono):
                taulukko_kopio = self.lukujono
                self.lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_kopio, self.lukujono)
            return

        return

    def poista(self, n):
        kohta = -1

        for i in range(0, self.alkioiden_lkm):
            if n == self.lukujono[i]:
                self.lukujono[i] = 0

                for j in range(i, self.alkioiden_lkm - 1):
                    self.lukujono[j] = self.lukujono[j + 1]
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True

        return False

    def kopioi_lista(self, lista1, lista2):
        for i in range(0, len(lista1)):
            lista2[i] = lista1[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [self.lukujono[i] for i in range(0, self.alkioiden_lkm)]
    
    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            yhdiste_joukko.lisaa(i)

        for i in b_taulu:
            yhdiste_joukko.lisaa(i)

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            for j in b_taulu:
                if i == j:
                    leikkaus_joukko.lisaa(j)

        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            erotus_joukko.lisaa(i)

        for i in b_taulu:
            erotus_joukko.poista(i)

        return erotus_joukko

    def __str__(self):
        tulostus = "{"
        if self.alkioiden_lkm == 0:
            tulostus += "}"
        elif self.alkioiden_lkm == 1:
            tulostus += str(self.lukujono[0]) + "}"
        else:
            for i in range(0, self.alkioiden_lkm - 1):
                tulostus = tulostus + str(self.lukujono[i])
                tulostus = tulostus + ", "
            tulostus = tulostus + str(self.lukujono[self.alkioiden_lkm - 1])
            tulostus = tulostus + "}"
        return tulostus