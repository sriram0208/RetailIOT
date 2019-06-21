import json
fh=open("mouse_log.txt","r")
data={}
data["mouseActions"]=[]
while True:
    
    line=fh.readline()
    if ("" == line):
        print("file finished")
        break;
    lis=line.split(" ",2)
#    print(lis)
    
    data["mouseActions"].append({
            'date':lis[0],
            'time':lis[1],
            'action':lis[2]
        })
    #data["date"]=lis[0]
    #data["time"]=lis[1]
    #data["action"]=lis[2]
print(data)
with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)


#json_data=json.dumps(data)
#print(json_data)

