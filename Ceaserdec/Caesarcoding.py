
import json
class Data:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class EncrDecr:
    def __init__(self):
        self.data = None

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
        word = raw_input("Enter the word to encrypt")
        shift = input("Enter the shift")
        if self.askfor_encrword(word,shift) is False:
            pass
        else:
            return
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
        self.savecoding(word,initial,encrypted_word=joint,decrypted_word=None)
        print joint
        return joint

    def decrypt(self):
        word = raw_input("Enter the word to decrypt")
        shift = input("Enter the shift")
        initial = shift
        self.askfor_decrword(word,shift)
        list = []
        fixshift = shift
        for key in word:
            if key == " ":
                list.append(" ")
            else:
                shift = fixshift
                self.reverse()
                keyloc = self.findData(key)
                while shift is not 0:
                    shift = shift - 1
                    keyloc = keyloc.next
                list.append(keyloc.data)
        joint = "".join(list)
        self.savecoding(word,initial,decrypted_word=joint,encrypted_word=None)
        print joint

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

    def savecoding(self,word, shift,encrypted_word=None, decrypted_word=None):
        file = open("saved_data.json", "r")
        saved_data = json.load(file)
        if word not in saved_data:
            saved_data[word] = []
        saved_data[word].append({"encr": encrypted_word, "decr": decrypted_word, "shifted by": shift})
        file.close()
        file = open("saved_data.json", "w")
        file.write(json.dumps(saved_data))
        file.close()

    def askfor_encrword(self,word,shift):
        file = open("saved_data.json", "r")
        saved_data = json.load(file)
        if word in saved_data:
            for item in saved_data[word]:
                if item["shifted by"] == shift:
                    print "The encryption is: " + str(item["encr"])
                    return
        elif word not in saved_data:
            return False

    def askfor_decrword(self,word,shift):
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


list = EncrDecr()
list.EncrDecr_data(list)
list.encrypt()
list.decrypt()





















