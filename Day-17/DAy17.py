class User:
    def __init__(self,user_id,username):
        print("New Users begin Created!!!")
        self.id = user_id
        self.username = username


user_1 = User("001","Firaol")
print(user_1.username)
