# score=int(input("请输入你的分数："))
# grade=""
# if score<0 or score>100:
#     print("内容错误")
# else:
#     if score<60:
#         grade="e"
#     elif score<70:
#         grade="d"
#     elif score<80:
#         grade="c"
#     elif score<90:
#         grade=("b")
#     else:
#         grade=("a")
#     print("你的成绩是{0}，等级是{1}".format(score,grade))
#以上为常规复杂写法，现给予优化


score = int(input("请输入你的分数："))
grade ="ABCDE"
if score <0 or score >100:
    score =int(input("分数不符合规范，请重新输入："))
else :
    num =score//10
    if num<6:
        num=5
    print("你的成绩是：{0}，你的等级是{1}".format(score,grade[9-num]))

