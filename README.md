# Prettify JSON

With this script you can print a specified JSON file to the command line with a pretty formatting.

# Quickstart

Specify the path to a file when using this script from the command line.
```bash
$ python pprint_json.py <path to file>
```

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py station.json
[
    {
        "global_id": 1773538,
        "NameOfStation": "Китай-город",
        "ModeOnEvenDays": "открытие в 05:30:00; закрытие в 01:00:00",
        "Name": "Китай-город, вход-выход 3 в северный вестибюль",
        "Longitude_WGS84": "37.6309849",
        "Latitude_WGS84": "55.7567672",
        "ModeOnOddDays": "открытие в 05:30:00; закрытие в 01:00:00",
        "ID": 326,
        "Line": "Калужско-Рижская линия",
        "LittleFunctionalBPAAmount": 4,
        "BPAAmount": 4,
        "RepairOfEscalators": [],
        "geoData": {
            "type": "Point",
            "coordinates": [
                37.6309849,
                55.7567672
            ]
        }
    }
]

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
