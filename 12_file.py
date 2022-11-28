fp = open('./text.txt')

# print(fp.read())

#print(fp.readline())
#print(fp.readline())
#fp.close()
'''
for line in fp:
 print(line) 

fp.close()
'''

# Sin necesida de cerar el archivo
# r w a 
# r+ lee y agrega
# w+ lee y sobreescribe

with open('text.txt', 'r+') as fp:
  for line in fp:
    print(line) 
  fp.write('FIN actividades')

