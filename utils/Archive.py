import requests

URL = 'https://web.archive.org/save/{}'
HEADER = {
    'url': '{}',
    'capture_all': 'on',
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

def save_archive(url):
    HEADER['url'] = url
    r = requests.get(URL.format(url), headers=HEADER)
    return r.status_code

def main():
    while True:
        try:
            url = input('Enter URL: ')
            if url == 'exit':
                break
            status = save_archive(url)
            print(status)
        except KeyboardInterrupt:
            break
        except:
            print('error')
            continue
        else:
            print('success')
            continue
        finally:
            print('finally')
            continue
    print('end')
if __name__ == '__main__':
    main()