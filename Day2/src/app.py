# creating entry point for the application
import faker
from models.customer import Customer
from store.customerstore import CustomerStore
from view.customerview import CustomerView


"""
this is main entry point for the application. it imports the faker library
"""


def check():
    """
    this function creates
    call the customer store and view to display the customer
    """
    customer_store = CustomerStore(num_customers=100)
    customer_view = CustomerView(customer_store.customers)
    customer_view.display_customers()



    # fake = faker.Faker()
    # print(fake.name())



if __name__ == "__main__":
    check()
