import xmltodict

stream = open('sample.xml')

xml = xmltodict.parse(stream.read())

for e in xml['People']['Person']:
    print(e)