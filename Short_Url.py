import pyshorteners

link = input("Enter the link: ")

Shortener = pyshorteners.Shortener()

short_url = Shortener.tinyurl.short(link)

print(short_url)


