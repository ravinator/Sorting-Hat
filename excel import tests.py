import pandas as pd

vragen = pd.read_excel (r'C:\Users\ionmi\Documents\Python\Sorteerhoed'
                        '\Test_sheet.xlsx',sheet_name='vragen')
antwoorden = pd.read_excel (r'C:\Users\ionmi\Documents\Python\Sorteerhoed'
                            '\Test_sheet.xlsx',sheet_name='antwoorden')

vragen = vragen.applymap(str)
#vragen = str(vragen.split('\n'))
for vraag in vragen:
    print(vraag)
#ugay

