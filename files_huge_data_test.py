"""

for line in open('myfile','r').readlines():
do_something(line)

However, the readlines() function loads the entire file into memory as it runs

"""

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


f = open('really_big_file.txt')
for piece in read_in_chunks(f):
    print piece