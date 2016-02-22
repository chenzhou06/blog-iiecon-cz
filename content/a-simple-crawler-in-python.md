Title: A Simple Crawler in Python
Author: Chen Zhou
Date: 2015-11-10 16:30
Category: Programming
Tags: programming, python, webcrawler

This post will demonstrate step by step how to write a simple crawler
in Python. Specifically, our target website here is
[Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code) which
contains 780 tasks for practicing programming. The goal of this
article is writing a crawler to collect all tasks from it.

# Prerequisites

To fully understand this tutorial, although being an expert is not
necessary, you must have been at least familiar with the syntax of
Python. In addition, some experiences with
[URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator),
[HTML](https://en.wikipedia.org/wiki/HTML) and
[jQuery](https://en.wikipedia.org/wiki/JQuery) are required, which
means you should know some basic
[DOM](https://en.wikipedia.org/wiki/Document_Object_Model) and
[CSS](http://www.w3.org/Style/CSS/) operations.

Also, the package `pyquery` is used here to fetch web content and parse
HTML. Since it is built on `requests` and `lxml`, and installing
`lxml` on Windows can cause a lot of headaches,
[Anaconda](https://www.continuum.io/downloads), rather than the
official release of [Python](https://www.python.org/), is highly
recommended, if anyone wants to follow the instructions below
line by line.

# Crawling Strategy

The procedure implemented here to capture data from the Internet can
be briefed as follows:

* Generate a list of URLs from which we can get the web pages we are
  interested in.
* Choose an URL from the list generated above, get the web page and filter
  out the data.
* Save the data to whatever an SQL dataset or a text file. Here I am
  just saving the data into a text file.
* Repeat the previous steps until the list of URLs is exhausted.

In the case of Rosetta Code, all the URLs can be found in
[this page](http://rosettacode.org/wiki/Category:Programming_Tasks). First,
by analyzing that page, we can find how all the URLs are coded in the
HTML. Open this page with a web browser, right click on a hyperlink
of a task, then click the button "View Element" on the menu (any modern browser
should have this button). A small window would pop out at the bottom showing the
html tag tree and corresponding css attributions of that hyperlink.

![View Element: An Example](/images/crawler-view-element.PNG)

According to the HTML tags, the links we are finding are all in a
`div` element which has a class attribution of `mw-content-ltr`. In
jQuery syntax, we can easily get all `a` element in that `div` with
only a line of `div.mw-content-ltr li a`, which says "find a `div`
with class `nw-content-ltr` then get all elements `li` therein and return
all elements `a`. More information about jQuery syntax can be found in
the [jQuery Tutorial](http://www.w3schools.com/jquery/).

With the similar method, a pattern about how the tasks is presented in
their web pages can be detected. From the `view element` window, we can
identify the description of tasks at a `div` with a `class`
attribution of `mw-content-text`. And all data we want to take is
located between a `div.infobox` and a `table#toc`. However, the Rosetta
Code website do not bundle all paragraphs about a task into a
dedicated `div` element, it needs more manipulation to extract all data
out of a mess. Details would be presented in the following section.

The third step is to save the data we fetched from the web. There are
many sophisticated way to store data, here I just save them into plain
text files. If the targeted data are extremely huge, the storage
method should be a concern.

# Implementation

After the crawling procedure is sorted out, it is time to turn
them into real code.

The first step can be written as a function `index` which take an
start url `indexURL` as an argument (see code below). With the help of
class `pq` , which is an abbreviation of `PyQuery` and imported from
the package `pyquery`, the content of a whole page at which the
`indexURL` is pointed can be stored into an object `indexPage`. The
class `pq` can automatically go to the URL it received and fetch the whole page
down to the local computer. In depth, this is achieved by a popular
package `requests`. Then, passing the argument `div.mw-content-ltr li
a` to the object `indexPage` to get a list of `a` elements. In the end,
using a list comprehension to generate all URLs pointed to the tasks.

```{.python}
from pyquery import PyQuery as pq
import os
import datetime

BASEURL = "http://rosettacode.org"
INDEXURL = "http://rosettacode.org/wiki/Category:Programming_Tasks"

def index(indexURL):
    indexPage = pq(url=indexURL)
    aElements = indexPage("div.mw-content-ltr li a")
    baseURL = BASEURL
    return [baseURL + i.attr.href for i in aElements.items()]

```

The second procedure is to extract data (see code below). Using
the same method to store a whole page to an object `page` with
`pq(url=URL)` in which the `URL` comes from the lists generated above
and is passed to the function `content` as an argument. The `div` where the data is
presented can be drawn out with `page("div#mw-content-text")`. Then,
remove the element `div.infobox` which we do not need, gather all
content before `table#toc`, and assign the content into `task`.  The
function `content` at length returns a dictionary which contains the
title and description of that task.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{.python}
def content(URL):
    page = pq(url=URL)
    div = page("div#mw-content-text")
    div("div.infobox").remove()
    task = div("table#toc").prevAll()
    title = page("h1#firstHeading").text()
    return {"title": title, "task": task}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the function `content` has fetched the data, it can be passed to
function `save` to be stored into hard disk. Here the filename must be
carefully designed, which must not contain any illegal character. When
opening a file to write data, the encoding must be explicitly set as
Unicode, otherwise it would be very easy to throw an encoding error. The
function `save` takes a great advantage of package `os.path` to
handle path problem. The usage of this package can be found in the
[Python Documentation](https://docs.python.org/3.4/library/os.path.html).

```{.python}
def save(content):
    filename = "".join([c for c in content["title"] if c.isalpha() or
                        c.isdigit() or c==' ']).rstrip()
    txtfile = os.path.join(DATAFOLD, filename + ".txt")
    with open(txtfile, "w", encoding="utf-8") as f:
        f.write(str(content["task"].text()))
    return
```

Finally, combining the three functions with a `for` loop which
iterates all URLs generated from the function `index` completes this
simple crawler program. In the body of the loop, the function
`content` fetches data and passes it straight to the function
`save`. For every URL, this program will print a message about time
and address in console.

~~~~~~~~~~~~~~~~~~~~~~{.python}
def main():
    for url in index(INDEXURL):
        print("[{}] try {}\n".format(datetime.datetime.now(), url))
        save(content(url))
~~~~~~~~~~~~~~~~~~~~~~

The full code can be organized as below. Some protective procedures
are added to prevent some system errors. All fetched data are stored in
the `data` folder.


~~~~~~~~~~~~~~~~~~~~~{.python}
from pyquery import PyQuery as pq
import os
import datetime

BASEURL = "http://rosettacode.org"
INDEXURL = "http://rosettacode.org/wiki/Category:Programming_Tasks"

CURRENTPATH = os.getcwd()
if not os.path.exists("data"):
    os.mkdir("data")
DATAFOLD = os.path.join(CURRENTPATH, "data")

def index(indexURL):
    indexPage = pq(url=indexURL)
    aElements = indexPage("div.mw-content-ltr li a")
    baseURL = BASEURL
    return [baseURL + i.attr.href for i in aElements.items()]

def content(URL):
    page = pq(url=URL)
    div = page("div#mw-content-text")
    div("div.infobox").remove()
    task = div("table#toc").prevAll()
    title = page("h1#firstHeading").text()
    return {"title": title, "task": task}

def save(content):
    filename = "".join([c for c in content["title"] if c.isalpha() or
                        c.isdigit() or c==' ']).rstrip()
    txtfile = os.path.join(DATAFOLD, filename + ".txt")
    with open(txtfile, "w", encoding="utf-8") as f:
        f.write(str(content["task"].text()))
    return

def main():
    for url in index(INDEXURL):
        print("[{}] try {}\n".format(datetime.datetime.now(), url))
        save(content(url))


if __name__ == "__main__":
    main()
~~~~~~~~~~~~~~~~~~~~~

# Further Improvement

This program is of every limited usage. There are at least three
directions to improve this crawler.

* Most importantly, no anti anti-scraping method is involved in this
  program at all, which will make this crawler very fragile when the
  remote host drops the connection. A schedule might be implemented in
  the program to make it less acquisitive and keep our scraping
  action out of attention. Also, a pool of IP addresses can serve as
  proxies to make the crawler undetectable.
* In respect of the efficiency, the three steps can proceed
  simultaneously by using multiprocess, so that the function `content`
  need not to wait for the function `save` finishing its job.
* All these steps can be further abstracted as a general work-flow,
  which can be easily extended to other situations. At that time, we
  just need to specify the pattern of URLs and data, the rest of the
  work is just the same.
