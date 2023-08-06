import typer
from rich import print_json
from rich.progress import track
from .classmodule import API, Image
from glob import glob

def main(path: str, verbose: bool = False):
	"""Main function that gets called from the command line."""
	# Support unix wildcards (e.g ./*.jpg)
	file_paths = glob(path)
	images = []
	for file in file_paths:
		images.append(Image(path=file))

	addr = typer.prompt('Address')
	api = API()
	location = api.geocode(addr)
	print_json(data=location)

	image: Image
	for image in track(images, description='Processing...'):
		print(f'Setting {image.path} location')
		image.add_location(lat=location['lat'], long=location['long'])
		print(f'Set {image.path} location')


typer.run(main)
