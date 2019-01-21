class Users:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
class Moderator(Users):
    def __init__(self,username,password):
        super.__init(username, password)

class Admin(Moderator):
    def __init__(self,username,password):
        super.__init(username, password)

class Comments:
    def __init__(self, comments):
        self.comments = comments
        