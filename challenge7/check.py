class Check:
    def __init__(self):
        self.characternotmatch = 0

    def compare(self, string1, string2):
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                print("characters do not match: " + string1[i] + ", " + string2[i])
                self.characternotmatch += 1
                break
        return self.characternotmatch