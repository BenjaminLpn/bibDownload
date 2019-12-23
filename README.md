# bibDownload
Download BibTex from Bing automatically.

### Introduction
* It is a time consuming to download BibTex from website manually, especially when we have downloaded the references.
This script aims at downloading from academic sources from website automatically.

* Current version only can download from Bing. It is welcome to modify it to support more websites.
> Actually, I failed to download from Google Scholar because the environment of my PyCharm and SublimeText cannot access proxy VPN.

* Furthermore, I want to make a utilibility to search related works and collect their bibs together for better understanding of one research point.


### Usage
* It is necessary to download **BeautifulSoup** package.
* `papers`: Please input all of your paper titles to this variable.
* `search_website`: Prefix of academic search from Bing.
* In theory, this script analyze the elements and get the paper ID in Bing Library. And then get the whole BibTex. Finally, it is better to modify it to the format you want.