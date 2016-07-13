fileHandle = open('device_list(5).txt','r')
print("GCFB Serial Number List")
print("***********************")
for line in fileHandle:
    fields = line.split('|')
    for lineItem in fields:
        if 'FG60DP' in lineItem:
            print(lineItem)
        if 'GCFB' in lineItem:
            if 'GCFBfmg' not in lineItem:
                print(lineItem)
    
fileHandle.close()
