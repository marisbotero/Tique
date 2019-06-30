import csv
from clients.models import Client

class ClientServices:

    def __init__(self, table_name):
        self.table_name = table_name
    
    def create_client(self,Client):
        with open(self.table_name, mode ='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

