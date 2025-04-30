import os
import xml.etree.ElementTree as ET


def round_bbox_values(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)  # Ensure output directory exists

    for filename in os.listdir(input_folder):
        if filename.endswith(".xml"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            tree = ET.parse(input_path)
            root = tree.getroot()

            for obj in root.findall(".//object/bndbox"):
                for coord in ["xmin", "ymin", "xmax", "ymax"]:
                    value = obj.find(coord).text
                    try:
                        rounded_value = str(round(float(value)))
                        obj.find(coord).text = rounded_value
                    except ValueError:
                        print(f"Skipping invalid value in {filename}: {value}")

            tree.write(output_path)
            print(f"Updated {filename} -> {output_path}")


# Example usage: Replace paths with actual locations
input_folder = "dataset/annotations"
output_folder = "dataset/annotations_fixed"
round_bbox_values(input_folder, output_folder)
