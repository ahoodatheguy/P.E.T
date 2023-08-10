import typer
from .gps import app as gps
from .rating import app as rating

app = typer.Typer()

app.add_typer(gps, name='gps')
app.add_typer(rating, name='rating')

app()
