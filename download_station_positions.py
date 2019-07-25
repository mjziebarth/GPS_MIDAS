#!/bin/python
import urllib.request

# Load all station names:
with open('midas-station-names.csv','r') as f:
	names = f.readlines()

N = len(names)
for i in range(N):
	names[i] = names[i].strip('\n')

# Now for each station name, load corresponding web page and extract lon and lat:
lons = []
lats = []
for i in range(N):
	print(names[i],":")
	try:
		page = urllib.request.urlopen('http://geodesy.unr.edu/NGLStationPages/stations/' + names[i] + '.sta')
		page = page.readlines()
	
		for k,line in enumerate(page):
			line = line.decode('ascii').strip()
			if '<h4>Longitude:' in line:
				lons += [float(line.strip('<h4>Longitude:').strip('</h4>'))]
				# Lons are displayed last:
				break
			elif '<h4>Latitude:' in line:
				lats += [float(line.strip('<h4>Latitude:').strip('</h4>'))]
	except:
		print("   --> HTTP ERROR.")
		lons += [None]
		lats += [None]

assert len(lons) == N
assert len(lats) == N

with open('midas-station-positions.csv','w') as f:
	f.write('# Name, lon, lat\n')
	for i in range(N):
		if lons[i] is None:
			f.write('%s,\t%s,\t%s\n' % (names[i], 'NAN', 'NAN'))
		else:
			f.write('%s,\t%.3f,\t%.3f\n' % (names[i], lons[i], lats[i]))

print("success!")
