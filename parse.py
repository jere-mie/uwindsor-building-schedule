import re

term = 'F22'

with open(f'data/{term}.txt', 'r') as f:
    # each room booking starts with "Section"
    text = f.read().split('Section')

    # removing new lines
    text = [i.replace('\n', '').strip() for i in text]

    # removing online courses
    text = filter(lambda x: 'synchronous' not in x.lower(), text)
    
    # removing trailing stuff
    text = [re.sub(r',\w+', '', i) for i in text]

    # removing more trailing stuff
    text = [re.sub(r' \(-\).+', '', i) for i in text]

    # removing dates
    text = [re.sub(r'\d\d\d\d-\d\d-\d\d', '', i) for i in text]

    # grabbing the info
    text = [re.search(r"(M|T|W|TH|F|MW|TTH) (\d\d:\d\d) (AM|PM) (\d\d:\d\d(AM|PM))(BiologyBuilding|Erie Hall|Dillon Hall|Toldo HealthEducationCtr|Chrysler HallSouth|Chrysler HallNorth|OdetteBuilding|LambtonTower|Essex Hall|MemorialHall|HK Building|EducationBuilding|LeddyLibrary|West Library|FreedomWay|JackmanDramatic ArtCntre|O'NeilMedicalEduc Centr)[ ]*(B\d+|G\d+|\d+)", i) for i in text]

    # filtering out stuff
    text = [i.groups() if i is not None else '' for i in text]
    text = list(filter(lambda x: x != '', text))

# unique elems only
text = list(set(text))

# out file
f = open(f'data/{term}.js', 'w')

# writing the JS object
f.write(f"const data = [\n")
for i in range(len(text)):
    f.write(f'    {{"day":"{text[i][0]}", "start":"{text[i][1]+text[i][2]}", "end":"{text[i][3]}", "building":"{text[i][5]}", "room":"{text[i][6]}"}}' + ',\n' if i != len(text)-1 else '\n')
f.write(']')
f.close()
print(f'Successfully parsed {len(text)} room bookings!')
