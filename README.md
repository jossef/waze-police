# Waze Police Coordinates Scraper

A Python script that extracts police coordinates from the Waze Live Map API within specified regions in Israel.

## Prerequisites

- Python 3
- Required Python packages can be installed using:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/jossef/waze-police.git
    ```

2. Navigate to the project directory:

    ```bash
    cd waze-police
    ```

3. Run the script:

    ```bash
    python main.py
    ```

## Description

The script fetches police coordinates from the Waze Live Map API within predefined regions in Israel. It uses the Waze API to retrieve alerts of type "POLICE" within specified geographic coordinates.

The coordinates are then stored in CSV files under the `data` directory, with each row containing the timestamp, latitude, and longitude of the police alert.

## Configuration

Modify the `ISRAEL_COORDINATES` list in the script to adjust the geographic regions for which you want to fetch police coordinates.

## License

This project is licensed under the MIT License