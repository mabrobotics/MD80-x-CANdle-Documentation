import os
import json
import glob
import re

folder_to_scan = "./_static/firmware/"
output_file = "./_static/firmware/downloadable_list.json"

raw_base = "https://mabrobotics.github.io/MD80-x-CANdle-Documentation/md-firmware/"
html_base = "https://github.com/mabrobotics/MD80-x-CANdle-Documentation/tree/main/_static/firmware"

DEVICE_MAP = {
    "md": "md",
    "candle": "candle",
    "pds": "pds",
    "flasher":"flasher"
}

def generate_file_list():
    search_pattern = os.path.join(folder_to_scan, "*")
    files_data = []
    
    output_filename = os.path.basename(output_file)

    version_pattern = re.compile(r'v?(\d+(?:\.\d+)+)')

    for f in glob.glob(search_pattern):
        if os.path.isfile(f):
            filename = os.path.basename(f)

            if filename == output_filename:
                continue
            
            clean_path = f"_static/firmware/{filename}"

            name_only, extension = os.path.splitext(filename)
            ext_without_dot = extension.lstrip('.')
            
            if not ext_without_dot or ext_without_dot.isdigit():
                file_type = "file"
            else:
                file_type = ext_without_dot

            match = version_pattern.search(filename)
            if match:
                file_version = match.group(1) 
            elif "latest" in filename.lower():
                file_version = "latest"
            else:
                file_version = "unknown"

            tag_name = "unknown" 
            filename_lower = filename.lower()  
            
            for search_key, target_device in DEVICE_MAP.items():
                if search_key in filename_lower:
                    tag_name = target_device
                    break
            
            file_info = {
                "name": name_only,
                "tag": tag_name,
                "version":file_version,
                "type": file_type,
                "html_url": f"{html_base}{clean_path}",
                "download_url": f"{raw_base}{clean_path}"
            }
            
            files_data.append(file_info)
    
    with open(output_file, "w") as f:
        json.dump(files_data, f, indent=4)

if __name__ == "__main__":
    generate_file_list()