# Report of Monaco 2018 Racing

This project creates a Monaco 2018 race report by processing data from 
the start and finish log files,as well as the drivers' abbreviation file.
The report can be sorted by drivers, and also allows you to print the data of a particular driver.

## Setup

You need `python>3.10` to run this script.

Install this package:`pip install report-racing-vasiliy==0.0.1`

## Usage

To generate a report, run the following command:
```bash
python report.py --files <folder_path> --desc (--asc, defaul) --driver <driver_name>
```
The `--files` option is required and should be followed by the path to the folder containing the data files.

The `--desc` option is optional for descending order, and the default value is `--asc`.

The `--driver` option is optional and accepts a specific driver name to print data for.

## Data files

The data files  format:

Start log file  format: `<driver abbreviation><YYYY-MM-DD_HH:MM:SS.sss>`.
End log file  format: `<driver abbreviation> <YYYY-MM-DD_HH:MM:SS.sss>`.
The abbreviations file format: `<driver abbreviation> <driver_name>_<team_name>`.

## Output

The report will be printed in the  format:
```bash
<driver_name>                | <team_name>                | <race_time>
```

## Example

For example, to  report sorted in descending order for a specific driver 'Hamilton', you would run:
```bash
    python report.py --files "C:\data" --desc --driver 'Sebastian Vettel'
```
