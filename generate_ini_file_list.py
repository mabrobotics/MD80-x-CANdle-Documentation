import os
import glob
import re

folder_to_scan = "./_static/firmware/"
output_file = "./_static/firmware/api_download_82cc028h.ini"

raw_base = "https://mabrobotics.github.io/MD80-x-CANdle-Documentation/md-firmware/"
mirror_base = "https://mabrobotics.github.io/mab-documentation-devel-deploy/md-firmware/"

DEVICE_MAP = {
    "md": "MD",
    "candle": "CANDLE",
    "pds": "PDS",
    "flasher": "MD_FLASHER" 
}

def generate_ini_list():
    search_pattern = os.path.join(folder_to_scan, "*")
    grouped_assets = {}
    
    output_filename = os.path.basename(output_file)

    arch_pattern = re.compile(r'_(x86_64|arm64|armhf|aarch64|amd64)', re.IGNORECASE)

    for f in glob.glob(search_pattern):
        if os.path.isfile(f):
            filename = os.path.basename(f)

            if filename == output_filename or filename.endswith(".json"):
                continue

            name_only, extension = os.path.splitext(filename)
            filename_lower = filename.lower()
            
            tag_name = "UNKNOWN" 
            for search_key, target_device in DEVICE_MAP.items():
                if search_key in filename_lower:
                    tag_name = target_device
                    break

            arch_match = arch_pattern.search(name_only)
            if arch_match:
                arch = arch_match.group(1).lower()
                section_name = name_only[:arch_match.start()]
            else:
                arch = "default"
                section_name = name_only

            if section_name not in grouped_assets:
                grouped_assets[section_name] = {
                    "type": tag_name,
                    "files": {}
                }
            
            grouped_assets[section_name]["files"][arch] = filename

    with open(output_file, "w") as f:
        for section, data in grouped_assets.items():
            f.write(f"[{section}]\n")
            f.write(f"type={data['type']}\n")
            
            for arch, fname in data['files'].items():
                if arch == "default":
                    f.write(f"filename={fname}\n")
                else:
                    f.write(f"filename_{arch}={fname}\n")
                    
            f.write(f"base_url={raw_base}\n")
            f.write(f"base_url_mirror={mirror_base}\n")
            
            for arch, fname in data['files'].items():
                clean_path = f"_static/firmware/{fname}"
                full_link = f"{raw_base}{clean_path}"
                
                if arch == "default":
                    f.write(f"download_url={full_link}\n")
                else:
                    f.write(f"download_url_{arch}={full_link}\n")
                    
            f.write("\n")

if __name__ == "__main__":
    generate_ini_list()