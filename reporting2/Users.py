

class Users:
    def __init__(self):
        self.users = [{"id": 1, "name": "Moeez", "CNIC": "13-45545-454", "Email": "moeez@gmail.com", "Password": "sss","type":"admin"},
                         {"id": 2, "name": "saba", "CNIC": "13-45545-454", "Email": "saba@gmail.com", "Password": "B","type":"dos"},
                         {"id": 3, "name": "gaba", "CNIC": "13-45545-454", "Email": "sp1000", "Password": "B","type":"dos"}
                         ]
        self.id = 4
    def setId(self):
        return 4

    def SignUp(self,name,cnic,email,password):
        for i in range(len(self.users)):
            if self.users[i]['Email'] == email:
                print("email already exists")
                return

        self.users.append({"id": self.id, "name": name, "CNIC": cnic, "Email": email, "Password": password,"type":"admin"})
        self.id=self.id + 1

    def login(self,email,password):
        for i in range(len(self.users)):
            if self.users[i]['Email'] == email and self.users[i]['Password'] == password:
                return  True
        return False

