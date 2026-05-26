import requests
import os

print("Starting Automatic IT Tools Downloader...")
print("-" * 25)


tools_urls = {
    "Putty.exe": "https://the.earth.li/~sgtatham/putty/latest/w64/putty.exe",
    "Wireshark_Installer.exe": "https://1.na.dl.wireshark.org/win64/Wireshark-win64-4.2.5.exe"
}


download_folder = "IT_Tools"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)


for tool_name, url in tools_urls.items():
    print(f"Downloading {tool_name}...")
    
    file_path = os.path.join(download_folder, tool_name)
    

    response = requests.get(url, stream=True)
    response.raise_for_status()
    

    with open(file_path, "wb") as file:

        for piece in response.iter_content(100000):
            file.write(piece)
            
    print(f"Successfully saved to: {file_path}")
    print("-" * 20)

print("All IT tools downloaded successfully inside 'IT_Tools' folder!")