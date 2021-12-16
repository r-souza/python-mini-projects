import click
import core.main as main

@click.command()
@click.option('--domain', '-d', help='Domain to test against NxFilter.')

def app(domain):
    """
    Get domain categories using NxFilter.
    """
    if domain:
        main.get_category(domain)
    
    else:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()

if __name__ == '__main__':
    app()