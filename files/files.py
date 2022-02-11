# File objects
import os

BASE_DIR = os.getcwd()

# Not a good version
f = open(BASE_DIR + '/files/test.txt', 'r')
print(f.name)
f.close()


# Best version
with open(BASE_DIR + '/files/test.txt', 'r') as f:
    # Different ways to iterate through lines
    # Gets the firs 100 characters of each line
    # sizeToRead = 100
    # fContents = f.read(sizeToRead)
    # print(fContents)

    # f.seek() used to reestablish the reading position of
    # a file
    # f.seek(0)
    # f.tell() check in which position you're in

    with open(BASE_DIR + '/files/testCopy.txt', 'w') as cf:
        for line in f:
            print(line)
            cf.write(line)


# Working with images
with open(BASE_DIR + '/files/img.jpg', 'rb') as rf:
    with open(BASE_DIR + '/files/imgCopy.jpg', 'wb') as wf:
        chunkSize = 4096
        rfChunk = rf.read(chunkSize)
        while len(rfChunk):
            wf.write(rfChunk)
            rfChunk = rf.read(chunkSize)

        # or
        # for line in rf:
        #   wf.write(line)
        
 