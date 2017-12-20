# -*- coding: utf-8 -*-

"""
Parse a list of errors extracted from the FACe's pdf (simple copy paste to a txt) and return a pretty print of the resultant dict
"""

with open("errors_from_pdf.txt") as f:
    result = []
    for line in f.readlines():
        splitted_lines = line.split(" ")
        code = splitted_lines[0]
        content = " ".join(splitted_lines[1:]).replace("\n","")

        print('    "{code}": {opener}'.format(code=code, opener="{"))
        print('        "description": "{content}",'.format(content=str(content)))
        print('        "error": True,')
        print('        "scope": "invoice",')
        print('    },')
