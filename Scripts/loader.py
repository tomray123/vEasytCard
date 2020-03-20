import httplib2

h = httplib2.Http('.cache')
response, content = h.request("https://www.xcom.ru/upload/medialibrary/a11/logo_hp.png")
out = open('img.png', 'wb')
out.write(content)
out.close()