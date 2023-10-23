# GitHub Action to Purge Cloudflare Cache

A simple GitHub action to purge CloudFlare cache by Zone Name or Zone ID. 

## Environment Variables
## `CF_EMAIL_ADDR`
The Email address of Cloudflare account.
## `CF_API_KEY`
An API key is a token that you provide when making API calls.
## `CF_ZONE_NAME`
Name of the domain for which you want to clear the cache.
## `CF_ZONE_NAMES`
The list of Names of the domains for which you want to clear the cache.
## `CF_PAGE_COUNT`
Only if you have more than 20 zones, set this variable.
## `CF_ZONE_ID`
Zone ID: Your domain's cloudflare identifier.
## `CF_ZONE_IDS`
List of Zone IDS: Your domain's cloudflare identifier.

## Examples:

### Clear cache by Zone Name:

#### Run using CloudFlare API key, Email and Zone Name
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.1.2
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_NAME: ${{ secrets.CF_ZONE_NAME }}
```

#### Run using CloudFlare API key, Email, Zone Name and  Page count(default 20)
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.1.2
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_NAME: ${{ secrets.CF_ZONE_NAME }}
        CF_PAGE_COUNT: ${{ secrets.CF_PAGE_COUNT }}
```
#### Run using CloudFlare API key, Email and List of Zone Name
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.1.2
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_NAMES: ${{ secrets.CF_ZONE_NAME }}
```

#### Run using CloudFlare API key, Email, List of Zone Name and  Page count(default 20)
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.1.2
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_NAMES: ${{ secrets.CF_ZONE_NAME }}
        CF_PAGE_COUNT: ${{ secrets.CF_PAGE_COUNT }}
```

### Clear cache by Zone ID:

#### Run using CloudFlare API key, Email and Zone ID
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.1.2
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_ID: ${{ secrets.CF_ZONE_ID }}
```

#### Run using CloudFlare API key, Email, Zone ID and Page count(default 20)
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.1.2
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_ID: ${{ secrets.CF_ZONE_ID }}
        CF_PAGE_COUNT: ${{ secrets.CF_PAGE_COUNT }}
```
#### Run using CloudFlare API key, Email and List of Zone IDS
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.1.2
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_IDS: ${{ secrets.CF_ZONE_ID }}
```

#### Run using CloudFlare API key, Email, List of Zone IDS and Page count(default 20)
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.1.2
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_IDS: ${{ secrets.CF_ZONE_ID }}
        CF_PAGE_COUNT: ${{ secrets.CF_PAGE_COUNT }}
```