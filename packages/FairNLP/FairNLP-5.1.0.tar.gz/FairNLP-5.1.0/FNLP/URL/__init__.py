import re
import requests
from FNLP.Regex import Re as Regex
from F import LIST

"""
    -> URL HANDLING
-> One period vs Two Periods?
    - The idea is all URLs have either 1 or 2 periods in the string.
        1. "verge.com"
        2. "www.verge.com"
        - Outside of this, there are only slashes. No more periods.
    - We figure out which it is in the current url
        - if 1 period, sitename is before last period.
        - if 2 periods, sitename is inbetween two periods.
    - We then parse the url to find the base site name.
"""

def get_base_url(url):
    """ -> PUBLIC -> Extract Base Site Name from URL <- """
    try:
        url = remove_http(url)
        last_index = 0
        for char in url:
            if str(char) == "/":
                base = url[:last_index]
                return base
            last_index += 1
        return url
    except Exception as e:
        print(f"Failed to get base url. URL=[ {url} ], error=[ {e} ]")
        return url

# @DeprecationWarning
def get_site_name(url):
    """ -> DEPRECATED FOR BASE_URL -> Extract Base Site Name from URL <- """
    try:
        if verifyTwoPeriods(url):
            return extract_siteName_two_periods(url)
        return extract_siteName_one_period(url)
    except:
        return False

def remove_http(url):
    return url.replace("https://", "").replace("http://", "")

def extract_base_url(url: str):
    if Regex.contains_any(search_terms=["http://", "https://"], content=url):
        newUrl = url.replace("https://", "").replace("http://", "")
        index = 0
        last = len(newUrl)
        for char in newUrl:
            if index >= last-1:
                return newUrl.replace("/", "")
            if char == "/":
                return newUrl[:index].replace("/", "")
            index += 1
    else:
        index = 0
        last = len(url)
        for char in url:
            if index >= last-1:
                return url.replace("/", "")
            if char == "/":
                return url[:index].replace("/", "")
            index += 1
    return url

def extract_sub_reddit(url):
    slash_count = 0
    index = 0
    start = 0
    end = 0
    url = remove_http(url)
    for char in url:
        if char == "/":
            slash_count += 1
            if slash_count == 2:
                # do work
                start = index - 1
            if slash_count == 3 or index >= len(url):
                end = index
        index += 1
    return url[start:end]

# -> get_site_name HELPER for verifying URL has one or two periods.
def verifyTwoPeriods(url: str):
    """ PRIVATE """
    if type(url) not in [str]:
        return False
    count = 0
    try:
        for char in url:
            if char == '.':
                count += 1
        if count >= 2:
            return True
        return False
    except:
        return False


# -> get_site_name HELPER for urls with one period.
def extract_siteName_one_period(url):
    """ PRIVATE """
    if type(url) not in [str]:
        return False
    i = 0
    slash_count = 0
    removal_index = 0
    for char in url:
        if char == "/":
            slash_count += 1
            if slash_count == 2:
                removal_index = i + 1
        if char == '.':
            return url[removal_index:i]
        i += 1
    return url


# -> get_site_name HELPER for urls with two periods.
def extract_siteName_two_periods(url):
    """ PRIVATE """
    if type(url) not in [str]:
        return False
    temp = ""
    start = 0
    end = 0
    i = 0
    periodCount = 0
    lastChar = ''
    # -> Part 1
    for char in url:
        if char == '/' and lastChar == '/':
            start = i + 1
        if char == '.':
            periodCount += 1
            if periodCount == 2:
                end = i
        if end > 0:
            temp = url[start:end]
            break
        lastChar = char
        i += 1
    # -> Part 2
    n = 0
    match = ""
    for c in temp:
        if c == '.':
            match = temp[n + 1:]
        n += 1
    return match


def extract_data_src_url(content: str):
    """ EXPERIMENTAL (under development still) """
    new = content.split("https://")
    for item in new:
        test = Regex.contains(":", item)
        if test:
            continue
        if len(item) < 5:
            continue
        return "https://" + item
    return False


def is_valid_url(url):
    """ PUBLIC """
    try:
        response = requests.get(url)
        if response:
            print("URL is valid and exists on the internet")
            return True
    except requests.ConnectionError as e:
        print("URL does not exist on Internet, error=[ {e} ]")
        return False

def is_url(content: str):
    """ PUBLIC """
    try:
        if type(content) in [list, tuple]:
            for itemContent in content:
                match = re.search(r'http.?://.*/', add_http(itemContent))
                if match is not None:
                    return True, match.string
            return False, False
        else:
            match = re.search(r'http.?://.*/', add_http(content))
            return True, match.string if match is not None else False
    except Exception as e:
        print(f"Failed to regex findall. {content}, error=[ {e} ]")
        return False, False

def url_ends_with(url, *args):
    args = LIST.flatten(args)
    for item in args:
        if str(url).endswith(item):
            return True
    return False

bad_exts = [".png", ".jpg", ".jpeg", ".gif", ".pdf", ".css", ".js", ".webp", ".ico", ".mjs", "svg", ".woff2"]
def filter_out_bad_exts(urls):
    filtered_urls = []
    for inner_url in urls:
        if url_ends_with(inner_url, bad_exts):
            continue
        filtered_urls.append(inner_url)
    return filtered_urls

def find_urls_in_str(content: str):
    if type(content) is not str:
        content = str(content)
    match = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    newMatch = []
    if match:
        for item in match:
            newItem = clean_url(item)
            newMatch.append(newItem)
    return newMatch

def clean_url(url: str):
    if type(url) is not str:
        url = str(url)
    newUrl = url.replace("\'", "").replace(",", "").replace("\"", "")
    return newUrl


def add_http(content):
    if content.startswith("//") or not content.startswith("http"):
        url1 = "https:" + content
        return url1
    return content


def avoid_url(url, avoid_list):
    """ EXPERIMENTAL """
    base_url = extract_base_url(url)
    if Regex.contains_any(avoid_list, base_url):
        return True
    return False


def filter_out_avoid_list(urls: [], avoid_list: []):
    """ EXPERIMENTAL """
    filtered_urls = []
    for single_url in urls:
        base_url = extract_base_url(str(single_url))
        if Regex.contains_any(avoid_list, base_url):
            continue
        filtered_urls.append(single_url)
    return filtered_urls


if __name__ == '__main__':
    test = get_site_name("https://www.cnet.co/news/")
    print(test)