# -*- encoding: utf-8 -*-
import struct

infile = open('input_file.stl', 'rb') #import file
out = open('ASCII.stl', 'w') #export file

data = infile.read()


out.write("solid ")

for x in range(0,80):
    if not data[x] == 0:
        out.write(chr(data[x]))
    else:
        pass
out.write("\n")

faces = struct.unpack('I', data[80:84])[0]

for x in range(0,faces):
    out.write("facet normal ")

    offset = 84+x*50

    out.write(str(struct.unpack('f', data[offset:offset+4])[0]) + " ")
    out.write(str(struct.unpack('f', data[offset+4:offset+8])[0]) + " ")
    out.write(str(struct.unpack('f', data[offset+8:offset+12])[0]) + "\n")

    out.write("outer loop\n")

    for y in range(1,4):
        out.write("vertex ")

        offset = 84+y*12+x*50

        out.write(str(struct.unpack('f',data[offset:offset+4])[0]) + " ")
        out.write(str(struct.unpack('f',data[offset+4:offset+8])[0]) + " ")
        out.write(str(struct.unpack('f',data[offset+8:offset+12])[0]) + "\n")

    out.write("endloop\n")
    out.write("endfacet\n")

out.close()
print("end")