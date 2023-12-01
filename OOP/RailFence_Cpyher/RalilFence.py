class Cypher:
    def __init__(self, amount):
        self.num_of_rails = amount

    def __transcript(self, open_text):
        return open_text.lower().replace(" ", "").replace("*", "")
    
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

    
    # Version 1
    # Very first if/then algorithm sketch, without using Google or ChatGPT to encrypt it. 
    # Not the prettiest but it works.

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

    # Explanation on line 25
    def encryptV1(self, open_text):
        self.__open_text = self.__transcript(open_text)
        self.__text_len = len(self.__open_text)
        self.__rails = [[] for _ in range(self.num_of_rails)]
        self.__count = 0
        self.__process()
        self.__cipher_text = "".join([char for subarr in self.__rails for char in subarr])
        return self.__cipher_text
    
    # Solution a day later after a bit of Googling and thinking.

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
        
text = str(input("Enter text: "))
rail = int(input("Enter amount of rails: "))

print("Main version")
Encrypt = Cypher(rail).encrypt(text)
Decrypt = Cypher(rail).decrypt(Encrypt)
print("Encrypted message: ", Encrypt)
print("DeCrypted message: ", Decrypt)

print("\nVersion 1")
EncryptV1 = Cypher(rail).encryptV1(text)
Decrypt = Cypher(rail).decrypt(EncryptV1)
print("Encrypted message (V1): ", EncryptV1)
print("DeCrypted message: ", Decrypt)

