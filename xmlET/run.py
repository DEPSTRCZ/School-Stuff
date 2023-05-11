import xml.etree.ElementTree as ET
parsed = ET.parse('xmlET\plants.xml')
root = parsed.getroot()

for element in root.findall("PLANT"):
    if float(element.find("PRICE").text[1:]) <= 3.00:
        print(f"\n┌─────────────────────\n│ {element.find('COMMON').text}                           \n├───────────────────────\n│ {element.find('BOTANICAL').text}                            \n├───────┬────────────────┘\n│ {element.find('PRICE').text} │                            \n└───────┘")


