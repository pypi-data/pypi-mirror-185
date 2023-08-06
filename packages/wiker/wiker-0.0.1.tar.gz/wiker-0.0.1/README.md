# Wiker

library for wikipedia text dataset collection

# Installation

```
pip install wiker
```

# Quickstart

```python
from wiker import Wiker

wk = Wiker(lang='uz', first_article_link="Turkiston")

wk.run(scrape_limit=50)
```

### Another methods

```python
from wiker import Wiker

wk = Wiker(lang='uz', first_article_link="Turkiston")

wk.reader() # read the pre_urls.txt file and return the result as a list
wk.read_url_count() # The number of all links that read the pre_urls.txt file
wk.extra_file_writer() # if the pre_urls.txt file is empty, the function writes first_article_link to the file
wk.scraper() # Get all articles from links in pre_urls.txt file
wk.text_cleaner() # clean up the html and other tags in the retrieved articles
wk.next_urls() # get links for further scraping
wk.dir_scanner() # scan the "data" folder to count files
wk.cleaned_text_writer(text_dict=wk.text_cleaner()) # 
wk.post_url_writer(url_list=wk.scraper().keys()) # writing the name of the saved articles to the file
wk.pre_url_writer(url_list=wk.next_urls()) # write names in next_urls to files for next process
```
