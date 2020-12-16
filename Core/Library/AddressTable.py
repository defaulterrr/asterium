import string, random

class AddressTable:
    def __init__(self):
        self.table = {}
        self.addresses = []
        self.lines = []
        pass

    def __get_random_string(self):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(4))
        result_str = "gen_" + result_str
        return  result_str

    def push(self, value):
        address = self.__get_random_string()
        while address in self.table:
            address = self.__get_random_string()
        self.table[address] = value
        self.addresses.append(address)
        return address

    def print(self):
        for address in self.addresses:
            print(address + str(self.table[address]))

    def generate(self):
        for address in self.addresses:
            # print(self.address + " " + "word" + " " + str(self.value) + "\n")\
            if self.table[address] == 0:
                self.lines.append(address + ": " + "resw" + " " + str(1) + "\n")
            else:
                self.lines.append(address + ": " + "word" + " " + str(self.table[address]) + "\n")



        return "".join(self.lines)