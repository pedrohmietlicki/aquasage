import requests
class InfluxRepository:
    influx_url = "http://localhost:8086/api/v2/write"
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
    def saveData(self,timestamp, level):
        
        influxLine = f"data_measurement value={level} {timestamp}"
        response = requests.post(self.influx_url, params=self.params, headers=self.headers, data=influxLine)
        if response.status_code == 204:
            print("Dados enviados com sucesso!")
        else:
            print(f"Falha ao enviar dados: {response.status_code} - {response.text}")    