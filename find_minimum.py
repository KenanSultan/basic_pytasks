somelist = [12, 45, 87, 
                [65, 34, 76],
                [34, 76, 43,
                    [8, 446, 23, 48,
                        [23,56,43,787],
                        {"key1": 543, "key2": 65, "key3": [54,2,335,76]}
                    ],
                    54, 23, 76, 32
                ],
                23, 65, 
                {"key1": 54, "key2": 234, "key3": {"key1": 234, "key2": [1, 245, 56, 45, (45,3,34,56)]}}
                ,23, 765, 22, "techacademy", "python", "coding", "bootcamp"
           ]

min = 999999

def find_minimum(l):
    global min
    
    for i in l:
        if type(i) == int:
            if i < min:
                min = i
        elif type(i) == str:
            if len(i) < min:
                min = len(i)
        elif type(i) == dict:
            find_minimum(i.values())
        elif type(i) == list or tuple:
            find_minimum(i)
    
    return min

print(find_minimum(somelist))
