# spray_detector.py - Password Spray Attack Detector

from collections import defaultdict

ip_user_map = defaultdict(set)

with open("logs.txt", "r") as file:
    for line in file:
        if "LOGIN FAIL" in line:
            parts = line.strip().split()
            user = parts[5].split("=")[1]
            ip = parts[6].split("=")[1]
            ip_user_map[ip].add(user)

for ip, users in ip_user_map.items():
    if len(users) >= 3:
        print(f"⚠️  Possible password spray detected from IP {ip}: attempted logins for {len(users)} users")
