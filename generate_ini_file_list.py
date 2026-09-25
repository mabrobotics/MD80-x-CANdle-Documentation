import os
import glob
import re

folders_to_scan = [
    "./_static/firmware/*/"
]
output_file = "./_static/firmware/api_download.ini"

raw_base = "https://mabrobotics.github.io/MD80-x-CANdle-Documentation/_static/firmware/"
mirror_base = "https://mabrobotics.github.io/mab-documentation-devel-deploy/_static/firmware/"

DEVICE_MAP = {
    "md": "MAB_FILE",
    "candle": "CANDLE",
    "pds": "PDS",
    "flasher": "MD_FLASHER" 
}

SUBPATH_MAP = {
    "MD_FLASHER": "md/legacy/",
    "MD": "md/",
    "CANDLE": "candle/",
    "PDS": "pds/",
    "UNKNOWN": ""
}

KNOWN_EXTENSIONS = ['.exe', '.bin', '.hex', '.elf', '.zip', '.tar.gz', '.appimage', '.mab']

def generate_ini_list():
    grouped_assets = {}
    output_filename = os.path.basename(output_file)

    arch_pattern = re.compile(r'_(x86_64|arm64|armhf|aarch64|amd64)', re.IGNORECASE)

    for folder in folders_to_scan:
        search_pattern = os.path.join(folder, "*")
        
        for f in glob.glob(search_pattern):
            if os.path.isfile(f):
                filename = os.path.basename(f)

                if filename == output_filename or filename.endswith(".json"):
                    continue

                rel_path = os.path.relpath(f, "./_static/firmware/")
                rel_path = rel_path.replace("\\", "/") 
                
                filename_lower = filename.lower()

                name_only = filename
                for ext in KNOWN_EXTENSIONS:
                    if filename_lower.endswith(ext):
                        name_only = filename[:-len(ext)]
                        break
                
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
                
                grouped_assets[section_name]["files"][arch] = {
                    "filename": filename,
                    "rel_path": rel_path
                }

    with open(output_file, "w") as f:
        for section, data in grouped_assets.items():
            f.write(f"[{section}]\n")
            f.write(f"type={data['type']}\n")
            
            for arch, file_data in data['files'].items():
                if arch == "default":
                    f.write(f"filename={file_data['filename']}\n")
                else:
                    f.write(f"filename_{arch}={file_data['filename']}\n")
            
            subpath = SUBPATH_MAP.get(data['type'], "")
            f.write(f"base_url={raw_base}{subpath}\n")
            f.write(f"base_url_mirror={mirror_base}{subpath}\n")
            
            for arch, file_data in data['files'].items():
                full_link = f"{raw_base}{file_data['rel_path']}"
                
                if arch == "default":
                    f.write(f"download_url={full_link}\n")
                else:
                    f.write(f"download_url_{arch}={full_link}\n")
                    
            f.write("\n")

if __name__ == "__main__":
    generate_ini_list()
