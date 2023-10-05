class Cypher:
    def __init__(self, amount):
        self.num_of_rails = amount

    def __transcript(self, open_text):
        return open_text.lower().replace(" ", "")
        
    def encrypt(self, open_text):
        self.__open_text = self.__transcript(open_text)
        self.__text_len = len(self.__open_text)
        self.__rails = [[] for _ in range(self.num_of_rails)]
        self.__count = 0
        for char in self.__open_text:
            self.__rails[1]
        pass

    def decrypt(self, cipher_text):
        pass

test = Cypher(3).encrypt("Test")