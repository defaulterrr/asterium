import string, random

class AddressTable:
    def __init__(self):
        self.table = {}
        self.addresses = []
        self.namespaces = []
        pass

    def __get_random_string(self):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(4))
        result_str = "gen_" + result_str
        return  result_str

    def get_random_namespace(self, prefix="") -> str:
        rand = self.__get_random_string()
        while prefix+rand in self.namespaces:
            rand = self.__get_random_string()
        namespace = prefix + rand
        self.namespaces.append(namespace)
        return namespace

    def push(self, value=0, namespace="") -> str:
        ''' Takes value and namespace as arguments, returns randomized address under specified namespace
        Keyword arguments:
        value – specified initialization value (default: 0)
        namespace – specified namespace (default: "")
        '''
        randomString = self.__get_random_string()
        while namespace+"_"+randomString in self.table:
            randomString = self.__get_random_string()
        address = namespace+"_"+randomString
        self.table[address] = value
        self.addresses.append(address)
        return address

    def isPresent(self, address, namespace="") -> bool:
        if namespace+"_"+address in self.addresses:
            return True
        else:
            return False

    def __str__(self):
        output = "Address table_______\n"
        for address in self.addresses:
            output = output + "Address: {}\n".format(address)
        for namespace in self.namespaces:
            output = output + "Namespace: {}".format(namespace)
        return output

    # def print(self):
    #     for address in self.addresses:
    #         print(address + ": " + str(self.table[address]))

    def generate(self):
        # for address in self.addresses:
        #     # print(self.address + " " + "word" + " " + str(self.value) + "\n")\
        #     if self.table[address] == 0:
        #         self.lines.append(address + ": " + "resw" + " " + str(1) + "\n")
        #     else:
        #         self.lines.append(address + ": " + "word" + " " + str(self.table[address]) + "\n")



        # return "".join(self.lines)
        pass

        