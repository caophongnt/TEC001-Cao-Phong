from flask import Flask, jsonify
import json
app = Flask(__name__)
with open("airports.json", "r", encoding="utf-8") as f:
    airports = json.load(f)
@app.route("/airport/<icao>", methods=["GET"])
def get_airport(icao):
    for airport in airports:
        if airport["icao"] == icao.upper():
            result = {
                "icao": airport["icao"],
                "name": airport["name"],
                "city": airport["city"],
                "country": airport["country"]
            }
            return jsonify(result)
    return jsonify({"error": "Airport not found"}), 404
if __name__ == "__main__":
    app.run(debug=True)
