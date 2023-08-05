import requests
from pyfzf.pyfzf import FzfPrompt
from exiftool import ExifToolHelper
from rich.pretty import pprint

class API():
	def __init__(self):
		pass
	
	def geocode(self, addr: str) -> dict:
		"""Convert address to coordinates."""
		r = requests.get(f'https://geocode.maps.co/search?q={addr}')
		self.data = r.json()
		selection = self.choose_location()
		return selection
	
	def choose_location(self):
		"""Use fzf to select address in case of multiple results from self.geocode"""
		locations = []
		for i in self.data:
			locations.append({'name': i['display_name'], 'lat': i['lat'], 'long': i['lon']})
		location_names = [location['name'] for location in locations]

		# Select location with fuzzy finding
		fzf = FzfPrompt('fzf')
		selection = ' '.join(fzf.prompt(location_names, '-i --border=rounded --cycle --reverse'))
		
		for location in locations:
			if selection == location['name']:
				# Coordinates of selected location.
				lat = location['lat']
				long = location['long']
		return {'name': selection, 'lat': lat, 'long': long}

class Image:
	def __init__(self, path: str):
		self.path = path
		self.exiftool = ExifToolHelper()
		self.exifdata = self.exiftool.execute_json('-k', self.path)

	@property
	def gps_coords(self):
		data = {
			'lat': self.exifdata[0]['Composite:GPSLatitude'],
			'long': self.exifdata[0]['Composite:GPSLongitude']
		}
		return data
	
	def add_location(self, lat:float, long:float):
		self.exiftool.execute_json('-GPSLatitudeRef=N', '-GPSLongitudeRef=W', f'-GPSLatitude={lat}', f'-GPSLongitude={long}', self.path)