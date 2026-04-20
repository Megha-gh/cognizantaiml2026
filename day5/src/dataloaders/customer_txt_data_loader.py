# import pandas as pd
# from dataloaders.customer_data_loader import CustomerDataLoader
# from store.customer_store_impl import CustomerStoreImpl
# from models.customer import Customer
# from models.full_name import FullName


# class CustomerTXTDataLoader(CustomerDataLoader):

#     def load_data(self, file_path, customer_store: CustomerStoreImpl):
#         with open(file_path, "r") as f:
#             data = f.read().splitlines()
#             df = pd.DataFrame(data, columns=['raw_data'])

#         for _, row in df.iterrows():
#             customer_id = row['customer_id']
#             first_name = row['first_name']
#             last_name = row['last_name']
#             email = row['email']
#             phone_no = row['phone_no']

#             full_name = FullName(
#                 first_name=first_name,
#                 last_name=last_name
#             )

#             customer = Customer(
#                 customer_id=customer_id,
#                 name=full_name,
#                 email=email,
#                 phone_no=phone_no
#             )

#             customer_store.add_customer(customer)

import pandas as pd
from dataloaders.customer_data_loader import CustomerDataLoader
from store.customer_store_impl import CustomerStoreImpl
from models.customer import Customer
from models.full_name import FullName


class CustomerTXTDataLoader(CustomerDataLoader):

    def load_data(self, file_path, customer_store: CustomerStoreImpl):

        customers = []
        customer_data = {}

        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()

                if not line and customer_data:
                    customers.append(customer_data)
                    customer_data = {}
                    continue

                if line.startswith("Customer"):
                    continue

                if ":" in line:
                    key, value = line.split(":", 1)
                    customer_data[key.strip()] = value.strip()

            if customer_data:
                customers.append(customer_data)

        df = pd.DataFrame(customers)

        for _, row in df.iterrows():
            customer_id = row['customer_id']
            first_name = row['first_name']
            last_name = row['last_name']
            email = row.get('email') or row.get('emai')  # handles typo
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