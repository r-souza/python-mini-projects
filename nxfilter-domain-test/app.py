import click
import core.main as main

@click.command()
@click.option('--domain', '-d', multiple=True, help='Domain to test against NxFilter. You can specify multiple domains by using multiple -d options. E.g. -d example.com -d example.org')

def app(domain):
    """
    Get domain categories using NxFilter.
    """
    if domain:
        if isinstance(domain, tuple):
            domains = set(domain)
            main.get_categories(domains)
        else:
            main.get_category(domain)
    
    else:
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        ctx.exit()

if __name__ == '__main__':
    app()