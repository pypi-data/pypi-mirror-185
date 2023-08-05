# FilMoreBlanks
## CSV File fill-in-the-blank Editor

FilMoreBlanks take a CSV and parses it for a specific string and fills that value with a chosen value. This works from 1:1 to 1:many value swaps.

## Getting started
- Place the CSV in the project main dir (for manual moves)
- fill out the config.yaml file that is located in the examples folder
- run the script using the quick start below
- POOF 💨
- you have a CSV that's just that much more useful to you 

## Files being moved
- processed files will move to the filled_files dir (Will be created in project path)
- the CSV used in the script will be moved to the archived dir (Will be created in project path)
- Config file will be moved to FilMoreBlanks_Configs (Will be created in project path)


## Quick Start
```bash
# move the config file to the project dir when running (recommended)
python3 basic_access.py -config_file config.yaml
```

## using as an import
when using as an import it will create a class object of the completed work, no config files are needed since it interacts with the main function directly.
```bash
pip install FilMoreBlanks
```

```python
import pandas as pd
from FilMoreBlanks import blanket_fill

dat = pd.read_csv('test_csv.csv')
bf = blanket_fill.BlanketFill(df_data=dat)

config_dict = {
    "new servers": [
        '5,5,5,5',
        '2.2.2.2',
        '7,7,7,7'],
    "11.1.0.0/16": [
        "233.31.244.39",
        "100.19.68.193",
        '235.253.243.128',
        '232.151.66.30',
        '74.22.1.140'],
    '169.156.158.231': [
        '111.254.29.134',
        '96.20.144.254']
}

affect_only_columns_dict = {'11.1.0.0/16':'source'}
bf.fix_csv(config_dict=config_dict,affect_only_columns_dict=affect_only_columns_dict)
res = bf.filled_data
```
