import requests
import time

INPUT_FILE = "ips.txt"

def get_country_code(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url, timeout=3)
        data = response.json()
        return data.get("country", "N/A")
    except Exception as e:
        return f"Error"

def main():
    with open(INPUT_FILE, "r") as f:
        ips = [line.strip() for line in f if line.strip()]

    for ip in ips:
        country = get_country_code(ip)
        print(f"{ip} => {country}")
   

if __name__ == "__main__":
    main()
