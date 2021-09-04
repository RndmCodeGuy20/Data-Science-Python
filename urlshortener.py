import urlshortener


def shorten(url):
    link = pyshorteners.Shorteners()
    return link.tinyurl.short(url)


if __name__ == "__main__":
    url = input("Enter Link : ")
    print(shorten(url))
