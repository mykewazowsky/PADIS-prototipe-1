import shapefile
import json

# Open the shapefile
sf = shapefile.Reader("data/jawa-loss-prototipe.shp")

# Get the fields (skip the first one which is deletion flag)
fields = sf.fields[1:]
field_names = [field[0] for field in fields]

# Create GeoJSON structure
geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Iterate through shapes and records
for shape_record in sf.shapeRecords():
    shape = shape_record.shape
    record = shape_record.record

    print(f"Processing shape type: {shape.shapeType}")

    # Convert shape to GeoJSON geometry
    if shape.shapeType in [5, 15, 25]:  # POLYGON, POLYGONZ, POLYGONM
        # Handle both POLYGON and POLYGONZ
        if hasattr(shape, 'parts') and len(shape.parts) > 1:
            # Multi-part polygon
            parts = list(shape.parts) + [len(shape.points)]
            coordinates = []
            for i in range(len(parts) - 1):
                part_coords = shape.points[parts[i]:parts[i+1]]
                # Close the polygon if not already
                if part_coords[0] != part_coords[-1]:
                    part_coords.append(part_coords[0])
                # Take only x,y coordinates, ignore z
                part_coords = [[coord[0], coord[1]] for coord in part_coords]
                coordinates.append(part_coords)
        else:
            # Single part polygon
            coordinates = shape.points
            # Close the polygon if not already
            if coordinates[0] != coordinates[-1]:
                coordinates.append(coordinates[0])
            # Take only x,y coordinates, ignore z
            coordinates = [[coord[0], coord[1]] for coord in coordinates]
            coordinates = [coordinates]

        geometry = {
            "type": "Polygon",
            "coordinates": coordinates
        }
    else:
        # Handle other types if needed
        continue

    # Create properties from record
    properties = {}
    for i, value in enumerate(record):
        properties[field_names[i]] = value

    # Create feature
    feature = {
        "type": "Feature",
        "geometry": geometry,
        "properties": properties
    }

    geojson["features"].append(feature)

# Write to GeoJSON file
with open("data/jawa-loss-prototipe.geojson", "w") as f:
    json.dump(geojson, f, indent=2)

print("Shapefile converted to GeoJSON successfully!")
