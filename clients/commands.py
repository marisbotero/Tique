import click


@click.group()
def clients():
    """Maganes the clients Lifecycle """
    pass

def create(ctx,name,company,email,position):
    """Creates a new clients"""
    pass

def list(ctx):
    """List all clients"""
    pass

def update(client_uid):
    """Update a client"""
    pass

def delete(ctx):
    """Delete a client"""
    pass