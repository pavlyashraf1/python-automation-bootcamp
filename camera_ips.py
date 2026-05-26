import webbrowser, time
print("checking network cameras......")
time.sleep(1)
cameras_ip_list = [
    "192.168.1.6",
    "192.168.1.7",
    "192.168.1.8",
    "192.168.1.9",
    "192.168.1.10"
]
print(f"Found {len(cameras_ip_list)} cameras")
print("Opening Camera Dashboards in your browser...")
print("-" * 25)
for ip in cameras_ip_list:
    camera_url = "http://" + ip
    print(f"Opening dashboard for camera at {camera_url}")
    webbrowser.open(camera_url)
    time.sleep(0.3)
print("-" * 25)
print("All camera dashboards opened successfully! Done.")