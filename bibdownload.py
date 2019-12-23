# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import re

# Generate the key words for search website (format for bing).
papers=["A Systematic Evaluation of Transient Execution Attacks and Defenses", "Context-Sensitive Fencing Securing Speculative Execution via Microcode Customization"]
for paper_name in papers:
    paper_key=paper_name.split()
    search_key=""
    for i in paper_key:
        search_key=search_key+"+"+i

    # if possible add more sites to search.
    search_website = "https://cn.bing.com/academic/search?q=" # bing
    resp = urllib.request.urlopen(search_website+search_key)
    html=resp.read()

    soup=BeautifulSoup(html,'html.parser', from_encoding='utf-8')
    content = soup.select('.caption_cite')
    # TODO: what is the difference between "select" and "find_all".

    results=re.findall(r"paperid=\"(.+?)\"", content.__str__())
    if (len(results)==0):
        print("No results.")
    else:
        # print("The most possible result is:")
        print("\n")
        # access the bib website
        bib_site="https://academicapi.chinacloudsites.cn/Paper/Citation/"+results[0]+"?type=bibtex&encoded=0"
        resp=urllib.request.urlopen(bib_site)
        html=resp.read()

        # get bib information and replace "<br/>" to "\n"
        soup=BeautifulSoup(html,'html.parser', from_encoding='utf-8')
        content=soup.select("pre")
        bib=re.findall(r"@(.*)}}", content.__str__())

        # split to list for formatting
        temp = bib[0].split("<br/>")

        # format bibkey
        temp[0]=temp[0].replace(" ","")
        temp[0]=temp[0].replace(':,',',')

        # format title
        index=[i for i, x in enumerate(temp) if (x.find("title")!=-1)][0]
        temp[index].replace("{","\"{")
        temp[index].replace("}","}\"")

        # add \n for each line
        for i in range(len(temp)-1):
            temp[i]=temp[i]+"\n  "
        bib_value=''.join(temp)

        print("@"+bib_value+"}\n}")