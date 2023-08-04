from setuptools import setup

setup(
	name="P.E.T",
	version="0.1.0",
	packages=["requests", "typer", "rich"],
	entry_points={
		"console_scripts": [
			"pet = pet.__main__:main"
	]
	}
)
