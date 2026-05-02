import tarfile
import os
import requests
import time

API_URL = "http://127.0.0.1:8000/validate/"

# =========================
# UI HACKER
# =========================
def banner():
    print("\033[92m")
    print("====================================")
    print("      iOS SYS SCANNER v1.0")
    print("====================================")
    print("\033[0m")

def loading(text):
    for i in range(3):
        print(f"{text}{'.' * (i+1)}")
        time.sleep(0.4)

# =========================
# KEY CHECK
# =========================
def check_key(key):
    try:
        r = requests.get(API_URL + key)
        return r.json().get("valid", False)
    except:
        print("[!] API offline")
        return False

# =========================
# EXTRAÇÃO
# =========================
def extract(file, out="dump"):
    loading("[*] Extracting sysdiagnose")
    with tarfile.open(file, "r:gz") as tar:
        tar.extractall(out)

# =========================
# SCANS
# =========================
def scan(root):
    proxy = []
    vpn = []
    certs = []

    vpn_keys = ["VPN", "IPSec", "IKEv2", "WireGuard", "OpenVPN"]

    for path, _, files in os.walk(root):
        for f in files:
            full = os.path.join(path, f)
            try:
                with open(full, "r", errors="ignore") as file:
                    data = file.read()

                    #
