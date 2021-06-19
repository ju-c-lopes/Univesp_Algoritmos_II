from urllib.request import urlopen

response = urlopen("http://www.w3.org/Consortium/mission.html")
page = response.read()
page = page.decode()
arq = open("site.html", "w")
arq.write(page)
arq.close()
