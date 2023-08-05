import typer
from rich import print_json
from .classmodule import API, Image
from glob import glob

def main(path: str, verbose: bool = False):
	# Support unix wildcards (e.g ./*.jpg)
	file_paths = glob(path)
	images = []
	for file in file_paths:
		images.append(Image(path=file))
	image: Image

	addr = typer.prompt('Address')
	api = API()
	location = api.geocode(addr)
	print_json(data=location)

if __name__ == '__main__':
	typer.run(main)
