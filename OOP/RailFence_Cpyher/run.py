class Cypher:
    def __init__(self, amount):
        self.num_of_rails = amount

    def __transcript(self, open_text):
        return open_text.lower().replace(" ", "")
    
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
        print(self.__rails)
            

    def decrypt(self, cipher_text):
        pass

#test = Cypher(3).encrypt("GEEKS FOR GEEKS")
test = Cypher(4).encrypt("THIS IS A SECRET MESSAGE")