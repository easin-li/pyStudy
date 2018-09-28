# -*- coding: UTF-8 -*-
import random

def auth_code():
    code = ''
    for i in range(5):
        number = str(random.randrange(1, 10))
        alphabet = chr(random.randrange(65, 91))
        code += random.choice([number, alphabet])
    return code

print (auth_code())


