# daylist=[]
# for m in range(6,13,1):
#     if(m==6 or m==9 or m==11):
#         for d in range(1,31,1):
#             if m<10:
#                 if d < 10:
#                     daylist.append('0'+str(m)+'0'+str(d))
#                 else:
#                     daylist.append('0'+str(m)+str(d))
#             else:
#                 if d < 10:
#                     daylist.append(str(m)+'0'+str(d))
#                 else:
#                     daylist.append(str(m)+str(d))
#     else:
#         for d in range(1,32,1):
#             if m<10:
#                 if d < 10:
#                     daylist.append('0'+str(m)+'0'+str(d))
#                 else:
#                     daylist.append('0'+str(m)+str(d))
#             else:
#                 if d < 10:
#                     daylist.append(str(m)+'0'+str(d))
#                 else:
#                     daylist.append(str(m)+str(d))
# print(daylist)
daylist=[]
for m in range(6,13,1):
    if(m==6 or m==9 or m==11):
        mm=31
    elif(m==12):
        mm=17
    else:
        mm=32
    for d in range(1, mm, 1):
        if m<10:
            if d < 10:
                daylist.append('0'+str(m)+'0'+str(d))
            else:
                daylist.append('0'+str(m)+str(d))
        else:
            if d < 10:
                daylist.append(str(m)+'0'+str(d))
            else:
                daylist.append(str(m)+str(d))
print(daylist)