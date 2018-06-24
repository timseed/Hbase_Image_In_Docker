import happybase

con=happybase.Connection(host='0.0.0.0')

print("Show the tables")
for a in con.tables():
     print("Table {}".format(a.decode()))

print("Dump the photo table")
tab = con.table(b'photo')

print('{}'.format(list(tab.scan())))

