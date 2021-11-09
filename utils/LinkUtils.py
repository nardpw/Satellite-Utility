from time import sleep
import requests, re
import subprocess

def findurls(text):
    """
    Finds all urls in a string
    """
    urls = re.findall('href="(.*?)"', text)
    return urls

def get_domain_with_url(url):
    r = re.search('(https?://.*?)/.*', url)
    if r is not None:
        return r.group(1)
    else:
        return None

def get_parts(link):
    """
    Returns the parts of a link.
    """
    parts = link.split('/')
    return parts

def convert_links_to_dict_tree(links):
    """
    Converts a list of links to a dictionary tree.
    """
    tree = {}
    for link in links:
        parts = get_parts(link)
        current = tree
        for part in parts:
            if part == '':
                continue
            if part not in current:
                current[part] = {}
            current = current[part]
    return tree

def remove_domain(url):
    """
    Removes the domain from the given URL.
    """
    domain = get_domain_with_url(url)
    if domain is not None:
        return url.replace(domain, '')
    else:
        return url

def remove_domain(list: list):
    """
    Removes the domain from the given list.
    """
    for i in range(len(list)):
        list[i] = list[i].replace(get_domain_with_url(list[i]), '')

def print_tree(dict, floor = 0):
    """
    Prints a tree of the given dictionary.
    """
    for key in dict:
        print(' ' * floor + key + '/')
        print_tree(dict[key], floor + 1)

async def tree(url, list, elapsed_urls, limit_domain = None):
    """
    Prints a tree of the given URL.
    """
    domain = get_domain_with_url(url)
    if url not in list:
        list.append(url)
        print(url)
        try:
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
            elapsed_urls.append(url)
            links = findurls(r.text)
            for link in links:
                if link.startswith('/'):
                    link = domain + link
                if limit_domain is None or get_domain_with_url(link) == limit_domain:
                    await tree(link, list, elapsed_urls, limit_domain)
        except requests.exceptions.MissingSchema:
            pass
        except:
            pass

def shrink(url):
    """
    Shrinks the given URL.
    """
    return requests.post('http://tinyurl.com/api-create.php', data={'url': url}).text

def youtube_dl(url):
    """
    Downloads the given YouTube URL.
    youtube-dl <url> --retries 10 --no-check-certificate --rm-cache-dir -f 18 -g
    """
    result = subprocess.check_output(['youtube-dl', url, '--no-playlist', '--retries', '10', '--no-check-certificate', '--rm-cache-dir', '-f', '18', '-g'], timeout=10)
    return result.decode('utf-8').strip()

# l = []
# base_url = 'https://spys.one/en/free-proxy-list/'
# tree(base_url, l, get_domain_with_url(base_url))
# # remove_domain(l)
# print(l)
# # d = convert_links_to_dict_tree(l)
# # print_tree(d)
'''youtube-dl https://www.youtube.com/watch?v=RmjL_IZkQAo --retries 10 --no-check-certificate --rm-cache-dir -f 18 -g'''