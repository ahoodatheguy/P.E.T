from setuptools import setup

setup(
	name="P.E.T",
	version="1.0",
	install_requires=["typer", "rich", 'pyexiftool'],
	entry_points={
		"console_scripts": [
			"pet = pet.__main__:main"
		]
	}
)
