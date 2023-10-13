import requests
import os

CF_API_URL = "https://api.cloudflare.com/client/v4"
CF_EMAIL_ADDR = os.environ.get("CF_EMAIL_ADDR")
CF_API_KEY = os.environ.get("CF_API_KEY")
CF_ZONE_NAME = os.environ.get("CF_ZONE_NAME")
CF_PAGE_COUNT = os.environ.get("CF_PAGE_COUNT")

def CFGetZoneIDByName(zone_name: str, headers: dict, per_page: str = None) -> str:

    if per_page is not None:
        request_url = f"{CF_API_URL}/zones?per_page={per_page}"
    else:
        request_url = f"{CF_API_URL}/zones"

    try:
        response = requests.get(request_url, headers=headers).json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    result = response["result"]

    for zone in result:
        if zone["name"] == zone_name:
            return zone["id"]
    return None

def CFPrugeZoneCache(zone_id: str, headers: dict) -> None:
    payload = {
        "purge_everything": True,
    }
    try:
        requests.post(f"{CF_API_URL}/zones/{zone_id}/purge_cache", headers=headers, json=payload)
        print(f"Zone ID: {zone_id} Cache purged successfully.")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
def main() -> None:

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": f"{CF_EMAIL_ADDR}",
        "X-Auth-Key": f"{CF_API_KEY}",
    }

    zoneID = CFGetZoneIDByName(CF_ZONE_NAME, headers, per_page=CF_PAGE_COUNT)
    CFPrugeZoneCache(zoneID, headers)

if __name__ == "__main__":
    main()