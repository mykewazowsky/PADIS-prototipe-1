import shapefile

# Open the shapefile
sf = shapefile.Reader("data/jawa-loss-prototipe.shp")

# Print the number of shapes
print("Number of shapes: {}".format(len(sf.shapes())))

# Print the fields
print("Fields:")
for field in sf.fields:
    print(field)

# Print the records
print("\nRecords:")
for record in sf.records():
    print(record)

# Print the shapes (first few)
print("\nFirst shape:")
if sf.shapes():
    shape = sf.shapes()[0]
    print("Shape type: {}".format(shape.shapeType))
    print("Number of points: {}".format(len(shape.points)))
    print("First 5 points: {}".format(shape.points[:5]))
    if hasattr(shape, 'parts'):
        print("Parts: {}".format(shape.parts))
