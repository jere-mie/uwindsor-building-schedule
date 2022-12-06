import pprint
import re
pp = pprint.PrettyPrinter(indent=4)
with open('F22.txt', 'r') as f:
    text = f.read().split('Section')
    text = [i.replace('\n', '').strip() for i in text]
    text = filter(lambda x: 'synchronous' not in x.lower(), text)
    text = [re.sub(r',\w+', '', i) for i in text]
    text = [re.sub(r' \(-\).+', '', i) for i in text]
    text = [re.sub(r'\d\d\d\d-\d\d-\d\d', '', i) for i in text]
    text = [re.search(r'(M|T|W|TH|F|MW|TTH) \d\d:\d\d (AM|PM) \d\d:\d\d(AM|PM)[\w ]+\d', i) for i in text]
    text = [i.group() if i is not None else '' for i in text]


# pp.pprint(text)
# print(text)
for i in text:
    print(i)
    print('------')