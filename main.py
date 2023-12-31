#!/usr/bin/env python3

import datetime
import requests
import os
import csv

ISRAEL_COORDINATES = [
    [33.394627725427384, 32.79753056823075, 34.69001770019532, 36.27204895019532],
    [32.970517754937156, 32.37054652510869, 34.58290100097657, 36.16493225097657],
    [32.513678453284, 31.910648507008453, 34.452438354492195, 36.034469604492195],
    [32.041119345469696, 31.434966177142343, 34.27734375000001, 35.85937500000001],
    [31.603543898629745, 30.994535847200826, 33.982772827148445, 35.564804077148445],
    [31.145686482685758, 30.533729624214832, 34.012985229492195, 35.595016479492195],
    [30.673796414232868, 30.058841660758542, 34.02603149414063, 35.60806274414063],
    [30.249427427175203, 29.631812634329865, 34.14550781250001, 35.72753906250001],
    [30.033282156922912, 29.414325653592105, 34.153060913085945, 35.735092163085945],
]


def get_police_coordinates_from_waze():
    headers = {
        "referer": "https://www.waze.com/he/live-map/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    total_alerts = dict()

    for coordinate in ISRAEL_COORDINATES:
        params = {
            "top": coordinate[0],
            "bottom": coordinate[1],
            "left": coordinate[2],
            "right": coordinate[3],
            "env": "row",
            "types": "alerts"
        }

        r = requests.get("https://www.waze.com/live-map/api/georss", headers=headers, params=params)
        r.raise_for_status()
        alerts = r.json().get('alerts', [])
        for alert in alerts:
            if alert['type'] != 'POLICE':
                continue

            alert_id = alert['uuid']
            total_alerts[alert_id] = alert

    locations = map(lambda x: dict(lat=x['location']['y'], long=x['location']['x']), total_alerts.values())
    locations = list(locations)
    return locations


def main():
    locations = get_police_coordinates_from_waze()
    if not locations:
        print('no locations found')
        return

    now = datetime.datetime.utcnow()
    now_epoch_millis = int(now.timestamp() * 1000)
    file_name = f"{now.strftime('%Y-%m-%d')}.csv"
    data_dir_path = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(data_dir_path, exist_ok=True)
    csv_file_path = os.path.join(data_dir_path, file_name)
    with open(csv_file_path, "a", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for location in locations:
            csv_writer.writerow([now_epoch_millis, location['lat'], location['long']])


if __name__ == '__main__':
    main()
