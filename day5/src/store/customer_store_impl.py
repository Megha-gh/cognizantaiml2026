#create customer store implementation from customer store abstract classification
from src.store.customer_store import CustomerStore
from src.exceptions.customer_not_found_exception import CustomerNotFoundException
class CustomerStoreImpl(CustomerStore):
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        raise CustomerNotFoundException(customer_id)

    def update_customer(self, customer_id, customer):
        for i in range(len(self.customers)):
            if self.customers[i].id == customer_id:
                self.customers[i] = customer
                return 
        raise CustomerNotFoundException(customer_id)
    def delete_customer(self, customer_id):
        for i in range(len(self.customers)):
            if self.customers[i].id == customer_id:
                del self.customers[i]
                return 
        raise CustomerNotFoundException(customer_id)