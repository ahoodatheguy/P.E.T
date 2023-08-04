from glob import glob
import requests
from pyfzf.pyfzf import FzfPrompt

class PET():
	def __init__(self, path: str):
		self.path = glob(path)
	
	def geocode(self, addr: str) -> dict:
		r = requests.get(f'https://geocode.maps.co/search?q={addr}')
		self.data = r.json()
		selection = self.choose_location()
		return selection
	
	def choose_location(self):
		locations = []
		for i in self.data:
			locations.append({'name': i['display_name'], 'lat': i['lat'], 'long': i['lon']})
		location_names = [location['name'] for location in locations]

		# Select location with fuzzy finding
		fzf = FzfPrompt('fzf')
		selection = ' '.join(fzf.prompt(location_names, '-i --border=rounded --cycle'))
		
		for location in locations:
			if selection == location['name']:
				# Coordinates of selected location.
				lat = location['lat']
				long = location['long']
		return {'name': selection, 'lat': lat, 'long': long}
