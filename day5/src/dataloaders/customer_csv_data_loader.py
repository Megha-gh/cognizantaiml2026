# #create customer CSV data loader implementation from customer data loader abstract class
# import pandas as pd
# from src.dataloaders.customer_data_loader import CustomerDataLoader
# from src.store.customer_store_impl import CustomerStoreImpl

# class CustomerDataLoader(CustomerDataLoader):
#     @abstractmethod
#     def load_data(self, file_path, customer_store:CustomerStoreImpl):
#         df = pd.read_csv(file_path)
#         for _, row in df.iterrows():#passing these fields in customer object
#             customer_id = int(row['customer_id'])
#             first_name = row['first_name']
#             last_name = row['last_name']
#             email = row['email']
#             phone_no = row['phone_no']
#             full_name = FullName(first_name=first_name, last_name=last_name)
#             customer = Customer(#creating customer object
#                 customer_id=customer_id,
#                 name=full_name,
#                 email=email,
#                 phone_no=phone_no
#             )# create customer CSV data loader implementation from customer data loader abstract class

import pandas as pd
from dataloaders.customer_data_loader import CustomerDataLoader
from store.customer_store_impl import CustomerStoreImpl
from models.customer import Customer
from models.full_name import FullName


class CustomerCSVDataLoader(CustomerDataLoader):

    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        df = pd.read_csv(file_path)

        for _, row in df.iterrows():
            customer_id = row['customer_id']
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            phone_no = row['phone_no']

            full_name = FullName(
                first_name=first_name,
                last_name=last_name
            )

            customer = Customer(
                customer_id=customer_id,
                name=full_name,
                email=email,
                phone_no=phone_no
            )

            customer_store.add_customer(customer)
#             customer_store.add_customer(customer)