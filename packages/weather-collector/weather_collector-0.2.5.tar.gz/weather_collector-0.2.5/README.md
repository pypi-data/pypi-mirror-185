# weather-collector

[![License: GPL v3](https://img.shields.io/badge/License-GPL_v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python Versions](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%20-blue) 
![Style Black](https://warehouse-camo.ingress.cmh1.psfhosted.org/fbfdc7754183ecf079bc71ddeabaf88f6cbc5c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667) 
[![status-badge](https://ci.codeberg.org/api/badges/cap_jmk/weather-collector/status.svg)](https://ci.codeberg.org/cap_jmk/weather-collector)


# Why 

Need to register a command to collect weather data in difficult environments and as part of other automatation tasks. For example, 
a regular, scheduled event triggers the collector. 

# What 

Build upon bulkhead to collect weather data without contaminating the package `bulkhead`
# Usage 

-o specifies the filename
-i specifies the interval in seconds 
-l the longitude
-t the latitude 
```bash
weather-collector -o /home/dev/Documents/weather-collector/sample.csv -i 1 -l 53.551086 -t 9.993682 
```

# Installation

## Production Build 

```bash 
pip install weather-collector
```

## Dev Build
Clone the repository with


### Linux 

Run with one of the following: 
```bash
bash install.sh
./install.sh
sh install.sh
```


### Windows

Double click on `install.bat` or run

```bash
install.bat
```

# Run sample 

Place .env file with parameters in the directory 

```bash 
OpenWeatherMapKey=key
OpenWeatherMapURL=api.openweathermap.org

TomorrowIOKey=key
TomorrowIOURL=api.tomorrow.io

```

For robustness consider using `screen`

```bash
sudo apt-get install screen
```

To detach press `CTRL+A,CTRL+D`

To get back to a session type

```bash
screen -r
```


```bash 
weather-collector -o ./sample.csv  -i 60 -l 53.551086 -t 9.993682 &
```