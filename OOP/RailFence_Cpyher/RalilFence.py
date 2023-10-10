class Cypher:
    def __init__(self, amount):
        self.num_of_rails = amount

    def __transcript(self, open_text):
        return open_text.lower().replace(" ", "").replace("*", "")
    
    # Vytvoří kolejnice, které se budou používat pro zašifrování textu. + Vyplní mezerami a hvězdičkami v patternu ZigZag
    def __create_rails(self, text):
        rails = [[ ' ' for _ in range(len(text))] for _ in range(self.num_of_rails)]
        row, col = 0, 0
        down = True

        for _ in range(len(text)):
            if row == 0: down = True
            if row == self.num_of_rails-1: down = False

            rails[row][col] = "*"
            col += 1

            if down: row += 1
            else: row -= 1
        return rails

    
    # Verze 1
    # Úplně první pokud/náčrt algoritmu, bez použití Googlu nebo ChatGPT na to jak to zašifrovat. 
    # Není nejhezčí ale funguje.

    def __process(self, down = True,):
        if down == True:
            tmp = 0

            for char in self.__open_text[self.__count:self.__count+self.num_of_rails]:
                self.__rails[tmp].append(char)
                tmp += 1

            self.__count += self.num_of_rails

            if self.__count <= self.__text_len:
                self.__process(False)

        else:
            tmp = self.num_of_rails-1

            for char in self.__open_text[self.__count:self.__count+(self.num_of_rails-2)]:
                tmp -= 1
                self.__rails[tmp].append(char)

            self.__count += self.num_of_rails-2

            if self.__count <= self.__text_len:
                self.__process(True)

    # Vysvětlení na řádku 25
    def encryptV1(self, open_text):
        self.__open_text = self.__transcript(open_text)
        self.__text_len = len(self.__open_text)
        self.__rails = [[] for _ in range(self.num_of_rails)]
        self.__count = 0
        self.__process()
        self.__cipher_text = "".join([char for subarr in self.__rails for char in subarr])
        return self.__cipher_text
    
    # Řešení o den později po trošce Googlení a přemýšlení.

    def encrypt(self, open_text):
        self.__open_text = self.__transcript(open_text)
        self.__text_len = len(self.__open_text)
        self.__rails = self.__create_rails(self.__open_text)

        for col in range(self.__text_len): # X
            for row in self.__rails: # Y
                if row[col] == "*":
                    row[col] = self.__open_text[col]
        cipher_text = "".join([char for subarr in self.__rails for char in subarr if char != " "])
        return cipher_text

    def decrypt(self, cipher_text):
        arr = self.__create_rails(cipher_text)

        down = True
        row, col = 0, 0
        tmp = 0
        result = ""
        for row in arr:
            for pos in range(len(row)):
                if row[pos] == "*":
                    row[pos] = cipher_text[tmp]
                    tmp += 1

        row, col = 0, 0
        for _ in range(len(cipher_text)):
            if row == 0:
                down = True
            if row == self.num_of_rails-1:
                down = False
            if (arr[row][col] != ' '):
                result += arr[row][col]
                col += 1
            if down: row += 1      
            else: row -= 1      
        return result
        
print("Hlavní verze")
print("TEXT: Tohle je tajná zpráva")
Encrypt = Cypher(3).encrypt("Tohle je tajná zpráva")
Decrypt = Cypher(3).decrypt(Encrypt)
print("Zašifrovaná zpráva: ", Encrypt)
print("Dešifrovaná zpráva: ", Decrypt)

print("\nVerze 1")
EncryptV1 = Cypher(3).encryptV1("Tohle je tajná zpráva")
Decrypt = Cypher(3).decrypt(EncryptV1)
print("Zašifrovaná zpráva (V1): ", EncryptV1)
print("Dešifrovaná zpráva: ", Decrypt)

