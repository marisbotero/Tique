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
    
    
    
def _print_welcome():
    print('Welcome Tique')
    print('*'*50)
    print('what would you like to do today?')
    print('[C]reate Client')
    print('[D]elete Client')
    print()
    
    

if __name__ == '__main__':
    _print_welcome()
    
    command = input()
    if command == 'C':
        client_name = input('What is the client name?')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid Command')