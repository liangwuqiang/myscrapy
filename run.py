from scrapy import cmdline

# cmdline.execute("scrapy crawl xici -o xici.csv".split())


# cmdline.execute("scrapy crawl tm_goods -o results.csv".split())
cmd = cmdline.execute("jupyter notebook")

print(cmd)

