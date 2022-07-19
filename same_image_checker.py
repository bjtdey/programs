import os, shutil
a=b=f=[]
d=e=0
p=r"/home/bijit/bijit/paperspoof_Repositeries/analysis/jan16/fake/image/paperspoof_v_0_5/"
a=os.listdir(r"/home/bijit/bijit/paperspoof_Repositeries/analysis/jan16/fake/image/paperspoof_v_0_5/fake_dest/")
b=os.listdir(r"/home/bijit/bijit/paperspoof_Repositeries/analysis/jan16/fake/image/paperspoof_v_0_5/m/")

for i in b:
    c=[]
    c=os.listdir(os.path.join(p, "m", i))
    print(c)
    for j in c:
        print(j)
        f.append(j)
#             c=os.path.join(p,i)
        e=e+1
for i in a:
    if i not in f:
        d+=1
        shutil.copy(str(os.path.join(p, "fake_dest", i)),str(os.path.join(p,"n",i)))
    print(f)           
print(d)





# for i in b:
#     if i not in a:
#         # c=os.path.join(p,i)
#         e=e+1
#         shutil.copy(str(os.path.join(p, "fake_dest", i)),str(os.path.join(p, "fake_dest_1", i)))
# # print(c)           
# print(e)


# for i in a:
#     c=[]
#     c=os.listdir(os.path.join(p, "me", i))
#     for j in :
#         if j in a:
#             c=os.path.join(p,i)
#             e=e+1
#             shutil.move(str(os.path.join(p, "shelf", j)),str(os.path.join(p,i)))
#     print(c)           
# print(e)
