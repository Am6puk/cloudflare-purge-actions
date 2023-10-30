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
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    result = response["result"]

    for zone in result:
        if zone["name"] == zone_name:
            return zone["id"]


def CFGetZoneIDByNames(zone_names: str, headers: dict, per_page: str = None) -> list:
    if per_page is not None:
        request_url = f"{CF_API_URL}/zones?per_page={per_page}"
    else:
        request_url = f"{CF_API_URL}/zones"

    try:
        response = requests.get(request_url, headers=headers).json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    result = response["result"]

    zone_ids_list = []

    for zone in result:
        if zone["name"] in zone_names:
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
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def CFPrugeZonesCache(zone_ids: str, headers: dict, payload: dict = None) -> None:
    if payload is None:
        payload = {
            "purge_everything": True,
        }
    for zone_id in zone_ids:
        try:
            requests.post(f"{CF_API_URL}/zones/{zone_id}/purge_cache", headers=headers, json=payload)
            print(f"Zone ID: {zone_id} Cache purged successfully.")
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


def main() -> None:

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": f"{CF_EMAIL_ADDR}",
        "X-Auth-Key": f"{CF_API_KEY}",
        "User-Agent": "github.com/Am6puk/cloudflare-purge-actions"
    }

    if CF_ZONE_ID is not None or CF_ZONE_IDS is not None:
        if CF_ZONE_ID is not None:
            CFPrugeZoneCache(CF_ZONE_ID, headers)
        else:
            CFPrugeZonesCache(CF_ZONE_IDS, headers)
    elif CF_ZONE_NAME is not None or CF_ZONE_NAMES is not None:
        if CF_ZONE_NAME is not None:
            zoneID = CFGetZoneIDByName(CF_ZONE_NAME, headers, per_page=CF_PAGE_COUNT)
            CFPrugeZoneCache(zoneID, headers)
        else:
            zoneIDS = CFGetZoneIDByNames(CF_ZONE_NAMES, headers, per_page=CF_PAGE_COUNT)
            CFPrugeZonesCache(zoneIDS, headers)
    else:
        raise SystemExit("No one of evns is set")


if __name__ == "__main__":
    main()
