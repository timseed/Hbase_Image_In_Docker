import happybase
from codecs import decode,encode
from glob import glob
import re
import hashlib
import daiquiri

def count_key(tab,key):
   res=tab.rows(key)
   #Res is a list
   if len(res)>0:
   #This is what res looks like for 2 records [(b'2', {b'cf:name1': b'juliet', b'cf:name2': b'dora'})]
   #It is a list with a tuple - inside is a dictionary
    return len(res[0][1])   #List item 0, Tuple object [1] (The dictionary)
   else:
     return 0

def calc_md5(obj):
    m = hashlib.md5()
    m.update(obj)
    return m.hexdigest()

def check_key_hash(tab,key,hash):
    # For the key ... does the hash already exist
    rv=False
    res=tab.rows(key)
    if len(res)>0:
      d=res[0][1]       
      for i in d.keys():
          ui=i.decode()
          if ui.startswith('cf:hash'):
             if d[i]==hash:
               break
      return True          
       
    return rv 

conn=happybase.Connection(host='0.0.0.0')
tab=conn.table(b'photo')
for file in sorted(glob("*.jpg")):
   id=re.findall('[1-9]+',file)[0]
   print("\n\nProcessing {}".format(file))
   print(    "ID         {}".format(id))
   with open(file,"rb") as imgfile:
        bin_data=imgfile.read()
        print("Binary Data Length is    \t{}".format(len(bin_data)))
        ascii_data=encode(bin_data,'base-64')
        print("binBinary Data Length is \t{}".format(len(ascii_data)))
        item_count=count_key(tab,id)
        print("key {} has  {} items already".format(id,item_count))
        hash=calc_md5(ascii_data)
        print("key {} hash {} ".format(id,hash))
        to_add=False
        if item_count>0:
           is_there=check_key_hash(tab,id,hash)
           if is_there==True:
               print("Sorry duplicate")
               print("{} is already added".format(id))
           else:
               print("Update for {}".format(id))
        else:
          #New Item it has an item_count of 0
          to_add=True
        if to_add:
           data={}
           #Columns are dynamic ... so create new columns
           image="cf:image{}".format(item_count+1).encode()
           md="cf:hash{}".format(item_count+1).encode()
           #data[image]=ascii_data
           data[image]=b'data'
           data[md]=hash.encode()
           tab.put(id.encode(),data)
           junk=1 
        
       

#tab.put(row, data, timestamp=None, wal=True)
#Docstring:
#Store data in the table.

#This method stores the data in the `data` argument for the row
#specified by `row`. The `data` argument is dictionary that maps columns
#to values. Column names must include a family and qualifier part, e.g.
#``b'cf:col'``, though the qualifier part may be the empty string, e.g.
#``b'cf:'``.
       
