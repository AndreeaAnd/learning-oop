print('Exceptii')
colors = ['red', 'green', 'blue']

try:
    # raise Exception('woo')
    colors[10]
except Exception as e:
    print(e)
else:
    print('nu avem erori')
finally:
    print('se executa intotdeauna')

