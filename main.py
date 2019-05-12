# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 21:44:01 2019

@author: maris
"""

    
import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Data Engineer',
    },
    {
        'name': 'Juan',
        'company': 'Facebook',
        'email': 'juan@facebook.com',
        'position': 'Data Scientist',
    },
]


def create_client(client):
    global clients

    if client_name not in clients:
        clients.append(client)
     
    else:
        print('Client already in client\'s list')


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']))



def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name       
    else:
        print('Client not in client\'s list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client not in client\'s list')


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True

def _get_client_field(field_name, message='What is the client {}?'):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_welcome():
    print('WELCOME')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client ={
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the new client name? ')

        update_client(client_name, updated_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')