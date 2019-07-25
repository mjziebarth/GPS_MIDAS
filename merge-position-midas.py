#!/bin/python

# Load all station positions:
with open('midas-station-positions.csv','r') as f:
	pos_lines = f.readlines()

pos_dict = dict()
for line in pos_lines:
	line = line.strip().replace(' ','').replace('\t','')
	if line[0] == '#':
		continue
	name,lon,lat = line.split(',')

	# For some stations, no location is known:
	if 'NAN' in lon:
		continue

	pos_dict[name] = (float(lon), float(lat))


# Load MIDAS data:
with open('midas.IGS08.txt','r') as f:
	midas_lines = f.readlines()

midas_dict = dict()
for line in midas_lines:
	line = line.strip()
	columns = line.split()
	name = columns[0]
	v_east    = float(columns[8])
	v_north   = float(columns[9])
	v_up      = float(columns[10])
	std_east  = float(columns[11])
	std_north = float(columns[12])
	std_up    = float(columns[13])
	midas_dict[name] = (v_east, v_north, v_up, std_east, std_north, std_up)


# Common stations in both files:
common = set(pos_dict.keys()) & set(midas_dict.keys())
print("common names:",len(common))
print("pos_dict:   :",len(pos_dict.keys()))
print("midas:       ",len(midas_dict.keys()))
print("only midas:  ",set(midas_dict.keys()) - common)

# Compose the common database:
names = sorted(list(common))
with open('midas-merged.csv','w') as f:
	f.write("# Table layout:\n")
	f.write('# Name, lon, lat, v_east, v_north, v_up, std_east, std_north, std_up\n')
	f.write('# velocities and standard deviations are given in m/yr (according to midas file)\n')
	for i,n in enumerate(names):
		numbers = (*pos_dict[n], *midas_dict[n])
		line = n + "," + ",".join(str(x) for x in numbers) + "\n"
		f.write(line)

print("done!")
