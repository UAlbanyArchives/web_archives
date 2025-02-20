# web_archives
A simple docker setup for web crawling into WARCs and WACZs

## Quickstart

```
docker compose up -d
docker exec -it ubuntu_wget bash
```
### Now your in Bash with wget and wacz installed

Make a folder for your web archives collection
```
mkdir [collection_name]
```

Run wget recursive at 3 levels
```
wget -r -l 3 -p --warc-file=[collection_name] --warc-cdx --convert-links --adjust-extension --span-hosts --no-parent -P data/[collection_name] [URL]
```

Convert to wacx
```
wacz create -o data/[collection_name].wacz data/[collection_name].warc.gz -t --detect-pages
```

#### Optionally create a pages.jsonl to review and pass that when creating the wacz
This will filter by domain:
```
python3 pages.py data/[collection_name].warc.gz "www.albany.edu"
wacz create -o data/[collection_name].wacz data/[collection_name].warc.gz -p data/[collection_name]_pages.jsonl
```

### Close the container
```
> exit
docker compose down
````

### Rebuilding the image from scratch
```
docker-compose build --no-cache
```
