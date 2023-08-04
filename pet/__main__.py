import typer
from rich import print_json
from .classmodule import PET
from glob import glob

def main(path: str, verbose: bool = False):
	files = glob(path)

	print(files)
	addr = typer.prompt('Address')
	pet = PET(path=path)
	print_json(data=pet.geocode(addr))


if __name__ == '__main__':
	typer.run(main)
