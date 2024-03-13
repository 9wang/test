def find_duplicated(lst):
    seen = set()
    duplicated = []
    for num in lst:
        if num in seen:
            duplicated.append(num)
        else:
            seen.add(num)
    return duplicated

Lst = [7,2,14,15,7,44,45,16,14,18,2,2,7,4,14,77,8,15,18]
duplicated = find_duplicated(Lst)
print(duplicated)

# no.2
sorted_duplicated = sorted(duplicated)
print(sorted_duplicated)

# no.3
import json

def classify_number(Lst):
    odd_dict = {}
    even_dict = {}
    for num in Lst:
        if num % 2 == 0:
            even_dict[str(num)] = num
        else:
            odd_dict[str(num)] = num

    result = {"odd": odd_dict, "even":even_dict}
    with open('F:/桌面/test2.josn','w') as file:
        json.dump(result,file)

classify_number(Lst)


# no.4

import pandas as pd

def write_to_excel(data,filename):
    df = pd.DataFrame(data)
    df.to_excel(filename,index=False)

with open('F:/桌面/test2.josn','r') as file:
    data = json.load(file)

write_to_excel(data,'F:/桌面/test2.xlsx')