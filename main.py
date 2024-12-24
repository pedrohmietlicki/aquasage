from datetime import datetime
import time
import requests

influx_url = "http://localhost:8086/api/v2/write"  # Ajuste a URL do InfluxDB
bucket = "my-bucket"  # Substitua pelo nome do seu bucket
org = "my-org"  # Substitua pelo nome da sua organização
token = "token"  # Substitua pelo seu token de acesso
headers = {
    "Authorization": f"Token {token}",
    "Content-Type": "text/plain"
}
params = {
        "org": org,
        "bucket": bucket,
        "precision": "s"
    }

data = {
    "2024-12-09 11:15": 1.78,
    "2024-12-09 11:30": 1.78,
    "2024-12-09 11:45": 1.77,
    "2024-12-09 12:00": 1.78,
    "2024-12-09 12:15": 1.77,
    "2024-12-09 12:30": 1.77,
    "2024-12-09 12:45": 1.78,
    "2024-12-09 13:00": 1.78,
    "2024-12-09 13:15": 1.78,
    "2024-12-09 13:30": 1.78,
    "2024-12-09 13:45": 1.78,
    "2024-12-09 14:00": 1.77,
    "2024-12-09 14:15": 1.77,
    "2024-12-09 14:30": 1.76,
    "2024-12-09 14:45": 1.76,
    "2024-12-09 15:00": 1.77,
    "2024-12-09 15:15": 1.77,
    "2024-12-09 15:30": 1.78,
    "2024-12-09 15:45": 1.78,
    "2024-12-09 16:00": 1.77,
    "2024-12-09 16:15": 1.77,
    "2024-12-09 16:30": 1.78,
    "2024-12-09 16:45": 1.78,
    "2024-12-09 17:00": 1.77,
    "2024-12-09 17:15": 1.77,
    "2024-12-09 17:30": 1.77,
    "2024-12-09 17:45": 1.76,
    "2024-12-09 18:00": 1.77,
    "2024-12-09 18:15": 1.77,
    "2024-12-09 18:30": 1.76,
    "2024-12-09 18:45": 1.76,
    "2024-12-09 19:00": 1.76,
    "2024-12-09 19:15": 1.76,
    "2024-12-09 19:30": 1.75,
    "2024-12-09 19:45": 1.75,
    "2024-12-09 20:00": 1.75,
    "2024-12-09 20:15": 1.74,
    "2024-12-09 20:30": 1.74,
    "2024-12-09 20:45": 1.74,
    "2024-12-09 21:00": 1.74,
    "2024-12-09 21:15": 1.73,
    "2024-12-09 21:30": 1.72,
    "2024-12-09 21:45": 1.71,
    "2024-12-09 22:00": 1.71,
    "2024-12-09 22:15": 1.71,
    "2024-12-09 22:30": 1.71,
    "2024-12-09 22:45": 1.71,
    "2024-12-09 23:00": 1.71,
    "2024-12-09 23:15": 1.7,
    "2024-12-09 23:30": 1.7,
    "2024-12-09 23:45": 1.69,
    "2024-12-10 00:00": 1.69,
    "2024-12-10 00:15": 1.69,
    "2024-12-10 00:30": 1.68,
    "2024-12-10 00:45": 1.68,
    "2024-12-10 01:00": 1.67,
    "2024-12-10 01:15": 1.67,
    "2024-12-10 01:30": 1.66,
    "2024-12-10 01:45": 1.65,
    "2024-12-10 02:00": 1.65,
    "2024-12-10 02:15": 1.65,
    "2024-12-10 02:30": 1.64,
    "2024-12-10 02:45": 1.64,
    "2024-12-10 03:00": 1.64,
    "2024-12-10 03:15": 1.64,
    "2024-12-10 03:30": 1.63,
    "2024-12-10 03:45": 1.63,
    "2024-12-10 04:00": 1.63,
    "2024-12-10 04:15": 1.63,
    "2024-12-10 04:30": 1.62,
    "2024-12-10 04:45": 1.62,
    "2024-12-10 05:00": 1.62,
    "2024-12-10 05:15": 1.61,
    "2024-12-10 05:30": 1.61,
    "2024-12-10 05:45": 1.61,
    "2024-12-10 06:00": 1.61,
    "2024-12-10 06:15": 1.6,
    "2024-12-10 06:30": 1.6,
    "2024-12-10 06:45": 1.6,
    "2024-12-10 07:00": 1.6,
    "2024-12-10 07:15": 1.6,
    "2024-12-10 07:30": 1.6,
    "2024-12-10 07:45": 1.6,
    "2024-12-10 08:00": 1.6,
    "2024-12-10 08:15": 1.61,
    "2024-12-10 08:30": 1.6,
    "2024-12-10 08:45": 1.6,
    "2024-12-10 09:00": 1.6,
    "2024-12-10 09:15": 1.6,
    "2024-12-10 09:30": 1.6,
    "2024-12-10 09:45": 1.61,
    "2024-12-10 10:00": 1.61,
    "2024-12-10 10:15": 1.61,
    "2024-12-10 10:30": 1.62,
    "2024-12-10 10:45": 1.61,
    "2024-12-10 11:00": 1.62,
    "2024-12-10 11:15": 1.63
}

river_level = []
def datetime_to_seconds(dt_str):
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    return int(time.mktime(dt.timetuple()))

measurement = "data_measurement"

for timestamp, value in data.items():
    ts_ns = datetime_to_seconds(timestamp)
    river_level.append(value)
    line = f"{measurement} value={value} {ts_ns}"
    response = requests.post(f"{influx_url}", params=params, headers=headers, data=line)
    if response.status_code == 204:
        print("Dados enviados com sucesso!")
    else:
        print(f"Falha ao enviar dados: {response.status_code} - {response.text}")    
print(river_level)