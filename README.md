# Processing MIDAS Data Files
Some scripts to process the raw MIDAS data tables from [UNR Geodesy](http://geodesy.unr.edu/).
In particular web retrieval of station positions.

See [this article](https://doi.org/10.1029/2018EO104623) to learn about this great data set.

## Usage
The ```download_station_positions.py``` script crawls the stations' websites to download
the station locations. Assumes that the MIDAS dataset is given (defaults to ```midas.IGS08.txt```
in the same directory), adjust filename if required.

The ```merge-positions-midas.py``` script then merges the MIDAS results with station
locations to create a data set of located GPS velocities.
