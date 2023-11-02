# try:
#     file = open('hello.txt', 'w')
#     file.write('Hello World')
#     raise Exception
# finally:
#     print('Vom inchide resursa')
#     file.close()

# or

with open('hello.txt', 'w') as f:
    f.write('Hello, Python!')
    raise Exception
