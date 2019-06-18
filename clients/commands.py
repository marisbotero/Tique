import click


@click.group()
def clients():
    """Maganes the clients Lifecycle """
    pass


@click.command()
@click.pass_context()
def create(ctx,name,company,email,position):
    """Creates a new clients"""
    pass


@click.command()
@click.pass_context()
def list(ctx):
    """List all clients"""
    pass


@click.command()
@click.pass_context()
def update(client_uid):
    """Update a client"""
    pass


@click.command()
@click.pass_context()
def delete(ctx):
    """Delete a client"""
    pass


all = clients