class Cypher:
    def __init__(self, amount):
        self.num_of_rails = amount

    def __transcript(self, open_text):
        return open_text.lower().replace(" ", "")
    
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


            
    def encrypt(self, open_text):
        self.__open_text = self.__transcript(open_text)
        self.__text_len = len(self.__open_text)
        self.__rails = [[] for _ in range(self.num_of_rails)]
        self.__count = 0
        self.__process()
        self.__cipher_text = " ".join(self.__rails)
        return self.__cipher_text
    
    def encrypt2(self, open_text):
        self.__open_text = self.__transcript(open_text)
        self.__text_len = len(self.__open_text)
        self.__rails = self.__create_rails(self.__open_text)
        self.__count = 0
        self.__process()
        self.__cipher_text = " ".join(self.__rails)
        return self.__cipher_text

    def decrypt(self, cipher_text):
        arr = [[ ' ' for y in range(len(cipher_text))] for _ in range(self.num_of_rails)]

        down = True
        row, col = 0, 0
        tmp = 0
        result = ""
        for _ in range(len(cipher_text)):
            if row == 0:
                down = True
            if row == self.num_of_rails-1:
                down = False
            arr[row][col] = "*"
            col += 1

            if down:
                row += 1
            else:
                row -= 1
        for row in arr:
            for pos in range(len(row)):
                if row[pos] == "_":
                    row[pos] = cipher_text[tmp]
                    tmp += 1


        row, col = 0, 0
        for i in range(len(cipher_text)):
            if row == 0:
                down = True
            if row == self.num_of_rails-1:
                down = False
            if (arr[row][col] != ' '):
                result += arr[row][col]
                col += 1
            if down: row += 1      
            else: row -= 1      
        print(arr)
        print(result)

    def test(self):
        print(self.__create_rails("GEEKSFORGEEKS"))
        

#test = Cypher(3).encrypt("GEEKS FOR GEEKS")
#test3 = Cypher(3).encrypt("GSGSEKFREKEOE")
#test2 = Cypher(4).encrypt("THIS IS A SECRET MESSAGE")

#dec = Cypher(3).decrypt("GSGSEKFREKEOE")
test = Cypher(3).encrypt2("GEEKS FOR GEEKS")
