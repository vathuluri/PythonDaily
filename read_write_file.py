file = open('dog_breeds.txt')

#try catch block;

reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()