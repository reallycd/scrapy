import hashlib
import re
from pathlib import Path
from urllib.parse import urlparse

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://tophub.today/"]

    browser_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
    }

    output_dir = Path("tophub_links_md")

    async def start(self):
        yield scrapy.Request(self.start_urls[0], headers=self.browser_headers, callback=self.parse)

    def parse(self, response):
        self.output_dir.mkdir(parents=True, exist_ok=True)

        seen_urls = set()
        for href in response.css("a::attr(href)").getall():
            if not href:
                continue
            href = href.strip()
            if href.startswith(("javascript:", "mailto:", "tel:", "#")):
                continue

            url = response.urljoin(href)
            if url in seen_urls:
                continue
            seen_urls.add(url)

            yield scrapy.Request(
                url,
                callback=self.parse_link,
                headers=self.browser_headers,
                meta={"source": response.url},
            )

    def parse_link(self, response):
        title = response.css("title::text").get(default="").strip()
        text_nodes = response.xpath("//body//text()[normalize-space()]").getall()
        text = "\n\n".join([node.strip() for node in text_nodes if node.strip()])
        text = text[:2000]

        markdown = [
            f"# {title or 'Untitled'}",
            "",
            f"- 原始链接: {response.url}",
            f"- 来源页面: {response.meta.get('source')}",
            f"- 状态码: {response.status}",
            "",
            "## 抽取文本预览",
            "",
            text or "（未提取到可用文本）",
        ]

        file_path = self.output_dir / self.url_to_filename(response.url)
        file_path.write_text("\n".join(markdown), encoding="utf-8")
        self.logger.info("Saved markdown for %s to %s", response.url, file_path)

    def url_to_filename(self, url):
        parsed = urlparse(url)
        path = parsed.path.strip("/") or "index"
        filename = f"{parsed.netloc}_{path}"
        if parsed.query:
            query = re.sub(r"[^A-Za-z0-9]+", "_", parsed.query)
            filename = f"{filename}_{query}"
        filename = re.sub(r"[^A-Za-z0-9_.-]+", "_", filename)
        filename = filename.strip("_.-") or "page"
        if len(filename) > 180:
            short_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
            filename = f"{filename[:150]}_{short_hash}"
        return f"{filename}.md"
