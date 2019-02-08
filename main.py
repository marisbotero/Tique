# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:44:01 2019

@author: maris
"""

    
clients = 'pablo,ricardo,'


def create_client(client_name):
    global clients
    clients += client_name
    _add_comma()
    
def list_clients():
    global clients
    print(clients)
    
def _add_comma():
    global clients
    clients += ','

if __name__ == '__main__':
    list_clients()
    create_client('david')
    list_clients()
   