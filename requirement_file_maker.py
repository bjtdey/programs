from dataclasses import replace


f=open("skopt_requirement.txt","r+")
new=[]
for lines in f: 
    for i in range(len(lines)):
        lines=lines.replace(" ","=")       
    for i in range(len(lines)):
        lines=lines.replace("===","==")
    new.append(lines)
    # new.append("\n")
# print(new)
f=open("skopt_requirement_req.txt","w")
for i in new:
    f.write(i)
f.close()
