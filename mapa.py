from flask import Flask, jsonify, request
import requests
import geopandas as gpd
from io import BytesIO

app = Flask(__name__)

WMS_URL = "https://sig.energia.gob.ar/wmsenergia"

@app.route("/get_data", methods=["GET"])
def get_data():
    layer = request.args.get("layer", "pozos_noinformados")
    bbox = request.args.get("bbox", "-7572157.770042702,-5756013.977986912,-7571546.273816421,-5755402.481760629")

    # Hacer una solicitud WMS para obtener la imagen de mapa
    params = {
        "service": "WMS",
        "request": "GetMap",
        "layers": layer,
        "styles": "",
        "format": "image/png",
        "transparent": "true",
        "version": "1.1.1",
        "width": 256,
        "height": 256,
        "srs": "EPSG:3857",
        "bbox": bbox
    }
    response = requests.get(WMS_URL, params=params)
    
    if response.status_code == 200:
        # Puedes procesar la imagen aquí, o devolver el mapa como JSON
        # Ejemplo para devolver datos ficticios en JSON
        print(response)
        data = {
            "layer": layer,
            "bbox": bbox,
            "message": "Este es un ejemplo, necesita más procesamiento para datos específicos."
        }
        return jsonify(data)
    else:
        return jsonify({"error": "No se pudo obtener la capa del servidor WMS"}), 500

if __name__ == "__main__":
    app.run(debug=True)
