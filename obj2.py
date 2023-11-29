class Effect:
    def ___init__(self, text: str, mag: int):
        self.__text = text
        self.__mag = mag

    @property
    def get_text(self):
        return self.__text

    @property
    def get_mag(self):
        return self.__mag

    def __str__(self):
        return f"{self.get_text} @ {self.get_mag}"

class Spell:
    ''' implements a spell
            >>> s = Spell()
            >>> s.add_effect(Effect('restore health', 40))
            >>> print(s)
            Spell: restore health @ 40, $40
            >>> s.add_effect(Effect('cure poison', 20))
            >>> print(s)
            Spell: restore health @ 40 + cure poison @ 20, $120
            >>> s.add_effect(Effect('restore health', 10))
            >>> print(s)
            Spell: restore health @ 40 + cure poison @ 20 + restore health @ 10, $140
            >>> s.change_effect_magnitude(2, 20)
            >>> print(s)
            Spell: restore health @ 40 + cure poison @ 20 + restore health @ 20, $160
        '''
    def __init__(self):
        self.__effect = []
        self.__value = 0

    def add_effect(self, effect: Effect):
        self.__effect.append([effect.get_text, effect.get_mag])

    def change_effect_magnitude(self, index: int, newmag: int):
        if index > len(self.__effect) - 1:
            raise IndexError("list index out of range")
        if newmag <= 0:
            raise ValueError("mag must not less than 0")
        self.__effect[index][1] = newmag

    @property
    def get_value(self):
        sm = 0
        check = 0
        for i in range(len(self.__effect)):
            h = 1
            txt = self.__effect[i][0]
            for j in range(len(self.__effect)):
                if self.__effect[j][0] == txt:
                    h = 0
            if h:
                check += 1
            sm += self.__effect[i][1]
        self.__value = int(sm * check)

    def __str__(self):
        txt = "Spell: "
        i = 0
        for ele in self.__effect:
            txt += ele[0] + ' @ ' + ele[1]
            if i == len(self.__effect) - 1:
                break
            i += 1
            txt += ' + '
        txt += f', ${self.__value}'
        return txt

s = Spell()
s.add_effect(Effect('restore health', 40))
print(s)