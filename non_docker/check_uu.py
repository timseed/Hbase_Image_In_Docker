from codecs import decode,encode
from glob import glob
for file in glob("*.jpg"):
   print("\n\nProcessing {}".format(file))
   with open(file,"rb") as imgfile:
        bin_data=imgfile.read()
        print("Binary Data Length is   \t{}".format(len(bin_data)))
        ascii_data=encode(bin_data,'base-64')
        print("Ascii Data Length is    \t{}".format(len(ascii_data)))
        #Just for fun we now will decode them
        bin_ascii_data = decode(ascii_data,'base-64')
        print("BinAscii Data Length is \t{}".format(len(bin_ascii_data)))
        if len(bin_ascii_data)==len(bin_data):
           print("Encode/Decode           \tOK")
        else:
           print("Encode/Decode           \tFAILED")

       
