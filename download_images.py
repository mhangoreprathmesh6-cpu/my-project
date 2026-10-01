from icrawler.builtin import GoogleImageCrawler

foods = ["biryani", "dosa", "idli", "samosa", "paneer curry"]

for food in foods:
    crawler = GoogleImageCrawler(storage={"root_dir": f"dataset/{food}"})
    crawler.crawl(keyword=food, max_num=200)