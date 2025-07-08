import requests
import time

INPUT_FILE = "ips.txt"

def get_ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}?fields=country,proxy,mobile,hosting"
        response = requests.get(url, timeout=3)
        data = response.json()
        
        country = data.get("country", "N/A")
        is_proxy = data.get("proxy", False)
        is_hosting = data.get("hosting", False)
        is_mobile = data.get("mobile", False)

        is_vpn = is_proxy or is_hosting  # hosting이 true면 대부분 VPN or server

        return country, is_vpn
    except Exception:
        return "N/A", "Error"

def main():
    with open(INPUT_FILE, "r") as f:
        ips = [line.strip() for line in f if line.strip()]

    for ip in ips:
        country, is_vpn = get_ip_info(ip)
        vpn_status = "VPN" if is_vpn is True else ("Not VPN" if is_vpn is False else is_vpn)
        print(f"{ip} => {country} => {vpn_status}")
        time.sleep(1)  # API 과속 방지

if __name__ == "__main__":
    main()
