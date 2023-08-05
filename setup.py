from setuptools import setup

setup(
	name="P.E.T",
	version="1.0",
	install_requires=["requests", "typer", "rich", 'pyexiftool', 'pyfzf'],
	entry_points={
		"console_scripts": [
			"pet = pet.__main__:main"
		]
	}
)
