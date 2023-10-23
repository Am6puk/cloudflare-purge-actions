import requests
import os

CF_API_URL = "https://api.cloudflare.com/client/v4"
CF_EMAIL_ADDR = os.environ.get("CF_EMAIL_ADDR")
CF_API_KEY = os.environ.get("CF_API_KEY")
CF_ZONE_NAME = os.environ.get("CF_ZONE_NAME")
CF_ZONE_NAMES = os.environ.get("CF_ZONE_NAMES")
CF_PAGE_COUNT = os.environ.get("CF_PAGE_COUNT")
CF_ZONE_ID = os.environ.get("CF_ZONE_ID")
CF_ZONE_IDS = os.environ.get("CF_ZONE_IDS")

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


def CFGetZoneIDByNames(zone_names: list, headers: dict, per_page: str = None) -> list:
    if per_page is not None:
        request_url = f"{CF_API_URL}/zones?per_page={per_page}"
    else:
        request_url = f"{CF_API_URL}/zones"

    try:
        response = requests.get(request_url, headers=headers).json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    result = response["result"]

    zone_ids_list = []
    for zone in result:
        for name in zone_names:
            if zone["name"] == name:
                zone_ids_list.append(zone["id"])

    return zone_ids_list


def CFPrugeZoneCache(zone_id: str, headers: dict, payload: dict = None) -> None:
    if payload is None:
        payload = {
            "purge_everything": True,
        }
    try:
        requests.post(f"{CF_API_URL}/zones/{zone_id}/purge_cache", headers=headers, json=payload)
        print(f"Zone ID: {zone_id} Cache purged successfully.")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def CFPrugeZonesCache(zone_ids: list, headers: dict, payload: dict = None) -> None:
    if payload is None:
        payload = {
            "purge_everything": True,
        }
    for zone_id in zone_ids:
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

    if CF_ZONE_ID is not None or CF_ZONE_IDS is not None:
        if CF_ZONE_ID is not None:
            CFPrugeZoneCache(CF_ZONE_ID, headers)
        else:
            CFPrugeZonesCache(list(CF_ZONE_IDS), headers)
    elif CF_ZONE_NAME is not None or CF_ZONE_NAMES is not None:
        if CF_ZONE_NAME is not None:
            zoneID = CFGetZoneIDByName(CF_ZONE_NAME, headers)
            CFPrugeZoneCache(zoneID, headers)
        else:
            zoneIDS = CFGetZoneIDByNames(list(CF_ZONE_NAMES), headers)
            CFPrugeZonesCache(zoneIDS, headers)
    else:
        raise SystemExit("No one of evns is set")


if __name__ == "__main__":
    main()
