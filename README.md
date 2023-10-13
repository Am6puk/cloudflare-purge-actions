# GitHub Action to Purge Cloudflare Cache

A simple GitHub action to purge CloudFlare cache by Zone Name. 

### Examples

#### Run using CloudFlare API key and Email
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.0.0
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_NAME: ${{ secrets.CF_ZONE_NAME }}
```

#### Run using CloudFlare API key, Email and Page count(default 50)
```yaml
    - name: Purge cache
      uses: am6puk/cloudflare-purge-actions@v1.0.0
      env:
        CF_EMAIL_ADDR: ${{ secrets.CF_EMAIL_ADDR }}
        CF_API_KEY: ${{ secrets.CF_API_KEY }}
        CF_ZONE_NAME: ${{ secrets.CF_ZONE_NAME }}
        CF_PAGE_COUNT: ${{ secrets.CF_PAGE_COUNT }}
```