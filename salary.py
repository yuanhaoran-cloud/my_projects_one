people_num=0
salarys=[]
salarys_sum=0
equal_salarys=0
while True:
    i = input("请输入薪资：（终止请按q）")
    if i.upper()=="Q":
        print("录入结束")
        break
    elif float(i)<0:
        print("数据错误！")
        continue
    else:
        salarys.append(float(i))
        salarys_sum+=float(i)
        people_num+=1
        equal_salarys=(salarys_sum/people_num)
print("总发人数：{0}，总发薪资:{1}，平均薪资:{2},具体表格：{3}".format(people_num,salarys_sum,equal_salarys,salarys))

