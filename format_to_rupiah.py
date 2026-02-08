import json

# Load the GeoJSON file
with open("data/jawa-loss-prototipe.geojson", "r") as f:
    geojson = json.load(f)

# Format the 'VALUE' field to Rupiah (multiply by 1 billion since it's percentage)
for feature in geojson["features"]:
    if "VALUE" not in feature["properties"]:
        # If VALUE is not present, set it to _majority
        feature["properties"]["VALUE"] = feature["properties"]["_majority"]
    value = feature["properties"]["VALUE"]
    # Multiply by 1 billion to convert percentage to Rupiah
    rupiah_value = value * 1000000000
    # Format as Rupiah: Rp followed by comma-separated number
    feature["properties"]["VALUE"] = "Rp {:,.0f}".format(rupiah_value)

# Save the updated GeoJSON
with open("data/jawa-loss-prototipe.geojson", "w") as f:
    json.dump(geojson, f, indent=2)

print("Values in GeoJSON have been formatted to Rupiah.")
