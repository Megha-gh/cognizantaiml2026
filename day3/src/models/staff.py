"""
create class staff inherits from person and associated to role
"""
from src.models.person import Person
class Staff(Person):#inheritance
    """
    Staff class inherits from Person
    """
    def __init__(self, adharCardNo: str, mobileNo: int, role: Role):
        super().__init__(adharCardNo, mobileNo)
        self.__role = role#association

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value
