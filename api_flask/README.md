# Build et lancer l'image docker :
Build
```bash
docker build -t
```

Lancer l'application
```bash
docker run -d -p 5000:5000 api_flask
```

# Tester une prédiction

Voici un exemple de requete :

```bash
curl --location --request POST 'http://localhost:5000/predict' --header 'Content-Type: application/json' --data-raw '{
    "HEIGHT": 5, "LENGTH": 7, "AREA": 35, "ECCEN": 1.400, "P_BLACK": 0.400, "P_AND": 0.657, "MEAN_TR": 2.33, "BLACKPIX": 14, "BLACKAND": 23, "WB_TRANS": 6
}'
```