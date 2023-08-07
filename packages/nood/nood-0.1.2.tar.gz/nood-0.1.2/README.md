# nood - Notifications On Demand

A wrapping library for web crawlers automation.

## Example Config

The configuration for each monitor is stored in a json file. The default
directory for the config file is the same as the monitor's script directory.
The default name for the config file is `config.json`, but can be configured
individually.

```json
{
  "siteId": 1234,
  "apiKey": "abcdefg1234567890",
  "proxies": [
    "ip:port:user:pass"
  ],
  "urls": [
    "https://example.com/1",
    "https://example.com/2"
  ],
  "pids": [
    "example-pid-1",
    "example-pid-2"
  ]
}
```

## Example Script

For each monitor, the `Scraper` and `Parser` class must be defined. The
monitoring logic is managed in the `Monitor` class which is defined by `nood`.

```python
import requests

from nood import monitor, objects


class KickzScraper(monitor.Scraper):
    def __init__(self, url: str, **kwargs):
        super(KickzScraper, self).__init__(url=url, **kwargs)

    def download(self) -> requests.Response:
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/108.0.0.0 Safari/537.36',
            'referer': 'https://www.kickz.com/.html',
        }
        response = self._s.get(
            url=self.url,
            proxies=self.get_static_proxy(),
            headers=headers
        )

        return response


class KickzParser(monitor.Parser):
    def __init__(self):
        super().__init__()

    def parse(self, *, response: requests.Response):
        return [objects.Product(
            url=response.url,
            name="TestProdukt"
        )]


if __name__ == "__main__":
    monitor.Monitor.launch_tasks(scraper=KickzScraper, parser=KickzParser)
```
