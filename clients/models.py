class Client:
    def __init__(self, name, company, email, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.positon = position
        self.uid = uid or uuid.uuid4()
    
    def to_dict(self):
        return vars(self)
    
    @staticmethod
    def schema():
        return['name', 'company', 'email', 'position', 'uid']
    
    