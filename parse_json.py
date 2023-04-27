import json

# Read the JSON file
with open('skateboard.mp4.json') as f:
    data = json.load(f)

# Initialize count for each specified name
specified_names = ['Walker', 'Bike', 'Skateboard', 'Scooter']
name_counts = {name: 0 for name in specified_names}

# Extract "left" value for each specified name and count occurrences
for entry in data:
    name = entry['Name']
    if name in specified_names:
        left_value = entry['Geometry']['BoundingBox']['Left']
        if left_value >= 0.2 and left_value <= 0.3:
            name_counts[name] += 1

# Print the count of occurrences for each specified name
for name in specified_names:
    count = name_counts[name]
    print(f"{name}: {count}")
