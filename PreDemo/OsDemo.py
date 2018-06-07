import os, sys
path = "D:/LI/Python/data"
os.rename("abc", "bca")
# 查看当前工作目录
retval = os.getcwd()
print ("当前工作目录为 " + retval)
# 修改当前工作目录

os.chdir( path )

# 查看修改后的工作目录
retval = os.getcwd()

print ("目录修改成功 %s" % retval)
print("i have")
print(os.listdir(path))