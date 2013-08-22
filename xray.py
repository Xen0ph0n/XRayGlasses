#! /usr/bin/python
# Xray allows an analyst to quickly generate a bitmap image of binary code
# This script was shared with me by a person who wishes to remain annonymous, has been tweeked by me, and is offered without licence.
# Chris@xenosec.org https://github.com/xen0ph0n/
import struct, argparse, os 

parser = argparse.ArgumentParser(description='Xray')
parser.add_argument('Filename', help='File To Be Scanned')
args = vars(parser.parse_args())
inputfilename = args['Filename']

b = bytearray(open(inputfilename, 'rb').read())
outputfilename = os.path.basename(inputfilename).split(".", 1)[0] + "___IMAGE.bmp"
outputfile = open(outputfilename, 'w')

# pad the end of the byte array so the length is a multiple of 256
if len(b) % 256 > 0:
	remainder = len(b) % 256
	padding = 256 - remainder
	for i in range(padding):
		b.append(0x00)

# start writing the static BMP header
outputfile.write("\x42\x4d\x36\x2c\x01\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x00\x01\x00\x00")
# build and write the height value in the header
height = len(b) / 256
heightbigendian = struct.pack('i', height)
outputfile.write(heightbigendian)
# finish writing the static BMP header
outputfile.write("\x01\x00\x18\x00\x00\x00\x00\x00\x00\x2c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# re-order the byte array so the top-left pixel will correspond with the first byte value
# this allows the image to be constructed left-to-right, top-to-bottom
output = bytearray()
for i in range(height, 0, -1):
	startval = ( i - 1 ) * 256
	stopval = startval + 256
	output.extend(b[startval:stopval])

# write each byte value 3 times to populate the BGR values for each pixel, producing a 256-shade grayscale output
# optionally, one or two BGR levels can be muted conditionally based on byte values (i.e. ASCII colorization)
for i in range(len(output)):
	a = chr(output[i])
	outputfile.write(a + a + a) 

outputfile.close()
print '[+] XRay Codeimage complete: ' + outputfilename 