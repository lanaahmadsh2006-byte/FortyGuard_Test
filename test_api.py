import requests

API_KEY = "66e2a3e291bd338dca6119ccf8df43f2"
submit_url = "https://api.fortyguard.com/v1/heatmap"

headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "polygon_aoi": {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [-74.0170, 40.7050],
                        [-74.0030, 40.7050],
                        [-74.0030, 40.7180],
                        [-74.0170, 40.7180],
                        [-74.0170, 40.7050]
                    ]]
                }
            }
        ]
    },
    "date_time": {
        "start_date": "2024-07-15",
        "start_time": "14:00",
        "filter_type": 1
    },
    "granularity": 100
}

try:
    response = requests.post(submit_url, headers=headers, json=payload)
    print("Status Code:", response.status_code)
    print("Response Data:", response.json())
except Exception as e:
    print("Error:", e)