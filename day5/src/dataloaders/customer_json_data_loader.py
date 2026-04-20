import json
import pandas as pd
from dataloaders.customer_data_loader import CustomerDataLoader
from store.customer_store_impl import CustomerStoreImpl
from models.customer import Customer
from models.full_name import FullName


class CustomerJSONDataLoader(CustomerDataLoader):

    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        with open(file_path, "r") as f:
            data = json.load(f)
            df = pd.DataFrame(data)

        
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