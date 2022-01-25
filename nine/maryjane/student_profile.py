class Profile(object):

    # constructor creation
    def __init__(self, firstname, lastname, phone_number, password) -> str:
        self.firstname = firstname

        self.lastname = lastname

        self.phone_number = phone_number

        self.password = password

    def __int__(self):
        pass

    #       getter and setter

    def get_first_name(self) -> str:
        return self.firstname

    def set_first_name(self, firstname):
        self.firstname = firstname

    def get_last_name(self) -> str:
        return self.lastname

    def set_last_name(self, lastname):
        self.lastname = lastname

    def get_phone_number(self) -> str:
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password
