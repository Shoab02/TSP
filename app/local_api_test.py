import requests

data = {
  "sl_no": 2,
  "ssc_p": 65.0,
  "hsc_p": 68.0,
  "degree_p": 64.0,
  "etest_p": 0,
  "mba_p": 57.8,
  "gender": "M",
  "ssc_b": "Central",
  "hsc_b": "Central",
  "hsc_s": "Arts",
  "degree_t": "Comm&Mgmt",
  "workex": "No",
  "specialisation": "Mkt&Fin"
}

response = requests.post('http://127.0.0.1:8000/predict',json=data)
print((response.text)[16:-3])




