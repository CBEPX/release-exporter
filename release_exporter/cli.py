import click


@click.group()
@click.option('--provider', help='github, gitlab or bitbucket.')
@click.option('--repo', help='Your repository name.')
@click.option('--token', help='Token number if its a private repository.', default=None)
@click.option('--tags', help='Range of tags.', default='all')
@click.option('--url',
              help="URL of your repository. This is optional if your current directory has .git folder with remote url.")
def cli(provider, repo, token, tags, url):
    pass


@cli.command(help='Creates .rex file.')
def init():
    pass


@cli.command(help='Creates markdown file.')
@click.option('--location', help='Where do you want to save your file.')
def markdown(location):


@cli.command(help='Creates JSON file.')
@click.option('--location', help='Where do you want to save your file.')
def json(location):
    pass


@cli.command(help='Creates YAML file.')
@click.option('--location', help='Where do you want to save your file.')
def yaml(location):
    pass
