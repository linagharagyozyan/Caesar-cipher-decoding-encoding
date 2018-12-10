import json
class Data:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class EncrDecr:
    def __init__(self):
        self.data = None

    def checkShift(self,shift):
        while True:
            try:
                int(shift)
                pass
            except ValueError:
                shift =raw_input("Value Error! Please enter integers")

    def EncrDecr_menu(self):
        ask = raw_input("Please choose one of the following(Please enter the number before the option)"
                        "\n""1.Encrypt"
                        "\n""2.Decrypt"
                        "\n""3.Exit")
        while True:
            if ask == "1":
                self.encrypt()
                self.EncrDecr_menu()
            elif ask == "2":
                self.decrypt()
                self.EncrDecr_menu()
            elif ask == "3":
                exit()
            else:
                ask = raw_input("Please enter a valid input")

    def append(self, data):
        newData = Data(data)
        temp = self.data
        if self.data is None:
            self.data = Data(data)
            self.data.next = self.data
            self.data.previous = self.data
        else:
            while temp.next is not self.data:
                temp = temp.next
            newData.previous = temp
            temp.next = newData
            newData.next = self.data
            self.data.previous = newData

    def reverse(self):
        next = None
        temp = self.data.previous
        while temp is not self.data:
            next = temp.previous
            temp.previous = temp.next
            temp.next = next
            temp = temp.next
        next = temp.previous
        temp.previous = temp.next
        temp.next = next
        self.data = temp.next

    def show(self):
        temp = self.data
        if temp.next == None:
            print 'empty list'
        else:
            while temp.next != self.data:
                print temp.data
                temp = temp.next
            print temp.data

    def findData(self, data):
        temp = self.data
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next

    def encrypt(self):
        word = raw_input("Enter the word/sentence to encrypt")
        while True:
            try:
                shift = input("Enter the shift")
                break
            except:
                print("That's not a valid option!")
        self.findEncrypted(word,shift)
        initial = shift
        list = []
        fixshift = shift
        for key in word:
            if key == " ":
                list.append(" ")
            else:
                shift = fixshift
                keyloc = self.findData(key)
                while shift is not 0:
                    shift = shift - 1
                    keyloc = keyloc.next
                list.append(keyloc.data)
        joint = "".join(list)
        self.saveCoding(word,initial,encrypted_word=joint,decrypted_word=None)
        print joint
        ask = raw_input("Continue Encrypting ??")
        while True:
            if ask.lower() == "yes":
                return self.encrypt()
            elif ask.lower() == "no":
                break
            else:
                ask = raw_input( "Please enter yes or no")

    def decrypt(self):
        word = raw_input("Enter the word/sentence to decrypt")
        while True:
            try:
                shift = input("Enter the shift")
                break
            except:
                print("That's not a valid option!")
        initial = shift
        self.findDecrypted(word,shift)
        list = []
        fixshift = shift
        for key in word:
            if key == " ":
                list.append(" ")
            else:
                shift = fixshift
                # self.reverse()
                keyloc = self.findData(key)
                while shift is not 0:
                    shift = shift - 1
                    keyloc = keyloc.previous
                list.append(keyloc.data)
        joint = "".join(list)
        self.saveCoding(word,initial,decrypted_word=joint,encrypted_word=None)
        print joint
        ask = raw_input("Continue Decrypting??")
        while True:
            if ask.lower() == "yes":
                return self.encrypt()
            elif ask.lower() == "no":
                break
            else:
                ask = raw_input( "Please enter a yes or no")

    def EncrDecr_data(self, list):
        letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u',
                         'v', 'w', 'x', 'y', 'z']
        for k in letters_lower:
            list.append(k)
        letters_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T',
                         'U', 'V', 'W', 'X', 'Y', "Z"]
        for k in letters_upper:
            list.append(k)
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for k in numbers:
            list.append(k)

    def saveCoding(self,word, shift,encrypted_word=None, decrypted_word=None):
        file = open("saved_data.json", "r")
        saved_data = json.load(file)
        if word not in saved_data:
            saved_data[word] = []
        saved_data[word].append({"encr": encrypted_word, "decr": decrypted_word, "shifted by": shift})
        file.close()
        file = open("saved_data.json", "w")
        file.write(json.dumps(saved_data))
        file.close()

    def findEncrypted(self,word,shift):
        file = open("saved_data.json", "r")
        saved_data = json.load(file)
        if word in saved_data:
            for item in saved_data[word]:
                if item["shifted by"] == shift:
                    print "The encryption is: " + str(item["encr"])
                    return
        elif word not in saved_data:
            return False

    def findDecrypted(self,word,shift):
        file = open("saved_data.json", "r")
        saved_data = json.load(file)
        if word in saved_data:
            for item in saved_data[word]:
                if item["shifted by"] == shift:
                    if item["decr"] is None:
                        pass
                    else:
                        print "The decription is: " + str(item["decr"])

        elif word not in saved_data:
            return False



def main():
    print "----------------------------""\n" "Welcome to **Caesar Cipher**""\n""----------------------------""\n"
    list = EncrDecr()
    list.EncrDecr_data(list)
    list.EncrDecr_menu()
main()


