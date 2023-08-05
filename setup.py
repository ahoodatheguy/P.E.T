from setuptools import setup, find_packages

setup(
	name="P.E.T",
	version="1.0",
	packages=find_packages(),
	install_requires=["requests", "typer", "rich", 'pyexiftool', 'pyfzf'],
	entry_points={
		"console_scripts": [
			"pet = pet.__main__:main"
		]
	}
)
