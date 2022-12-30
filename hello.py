import click
import glob

@click.command()
@click.option(
    "--path",
    prompt = "Path to search csv files",
    help = "this is the path to search for files: tmp",
)

@click.option(
    "--ftype", 
    prompt = "Pass in the type of file",
    help = "Pass in the file type: i.e csv"
    )

def search(path, ftype):
    results = glob.glob(f"{path}/and*.{ftype}")
    click.echo(click.style("Found Matches:", fg='red'))
    for result in results:
        click.echo(click.style(f"{result}", fg='white', bg='blue'))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    search()