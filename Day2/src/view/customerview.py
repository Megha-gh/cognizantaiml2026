import typing
from models.customer import Customer
class CustomerView:
    def __init__(self,customer_store:typing.List[Customer]):
        self.customer_store = customer_store
    def display_customers(self):
        for customer in self.customer_store:
            print(customer)
    def display_customers(self):
        for customer in self.customer_store:
            print(customer)
