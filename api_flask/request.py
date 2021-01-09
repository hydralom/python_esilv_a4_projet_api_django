import requests

url = 'http://127.0.0.1:5000/predict'  # localhost and the defined port + endpoint
body = {
    "HEIGHT": 5,
    "LENGTH": 7,
    "AREA": 35,
    "ECCEN": 1.400,
    "P_BLACK": 0.400,
    "P_AND": 0.657,
    "MEAN_TR": 2.33,
    "BLACKPIX": 14,
    "BLACKAND": 23,
    "WB_TRANS": 6
}
response = requests.post(url, data=body)
response.json()

"""
curl --location --request POST 'http://localhost:5000/predict' --header 'Content-Type: application/json' --data-raw '{
    "HEIGHT": 5, "LENGTH": 7, "AREA": 35, "ECCEN": 1.400, "P_BLACK": 0.400, "P_AND": 0.657, "MEAN_TR": 2.33, "BLACKPIX": 14, "BLACKAND": 23, "WB_TRANS": 6
}'

"""