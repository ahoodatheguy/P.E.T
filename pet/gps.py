"""Manage GPS data"""
import typer
from .funcmodule import parse_path
from .classmodule import API, Image
from rich import print_json, print
from rich.progress import track

app = typer.Typer()

@app.command('add')
def add_location(path: str):
	images = parse_path(path=path)
	"""Add location to list of images."""
	image: Image
	for image in images:
		if image.gps_coords is False:
			print(f'[blue]{image.path}[/blue] has no location.')
		else:
			print(f'Current location for [blue]{image.path}[/blue]: {image.gps_coords["lat"]}, {image.gps_coords["long"]}')

	addr = typer.prompt('Address')
	api = API()
	location = api.geocode(addr)
	print_json(data=location)

	image: Image
	for image in track(images, description='Processing...'):
		print(f'Setting {image.path} location to {location["lat"]}, {location["long"]}')
		image.add_location(lat=location['lat'], long=location['long'])
		print(f'Set {image.path} location to {image.gps_coords["lat"]}, {image.gps_coords["long"]}')
