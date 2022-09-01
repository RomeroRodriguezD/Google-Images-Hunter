# Google Images Hunter

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Google Images Hunter.

```bash
pip install google-images-hunter
```

## Usage

```python
from google_hunter_images import Searcher, ImageDownloader

# Step 1, create a Searcher object.
    searcher = Searcher()
# Step 2, set and trigger the scrap() function. Concept is a required parameter.
# Max_images and loadmore have default values. download_url_lists defaults as False.

mylist = searcher.scrap(concept='clown', download_url_lists=True, max_images=250, loadmore=20)

# Step 3, use the URl list generated by scrap() to download the images on a given path. Defaults to current path.

ImageDownloader(mylist, path='downloadtest/clowns/')
```

## Contributing

This is just an scraper I built since I have not been able to find the exact kind of Google images scraper I was looking for. I made it mixing my own ideas and some features I cherrypicked from different scraping scripts I found during my research task. Thanks to those anonymous contributors.

Pull requests are welcome. For changes, please open an issue first to discuss what you would like to change. Notice that this is the first version, currently tested on Firefox, so although it should
work regularly on Chrome and Edge, it still needs more tests.



## License
[MIT](https://choosealicense.com/licenses/mit/)