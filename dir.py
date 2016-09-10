import re
path = "dir\n\tddir\n\t\ta.txt\n\t\tb.jpeg\n\t\tc.gif\nddir2\n\tdddir\n\tddddir\n\t\taaa.jpg"
print path
#print path.replace("\n","/")
dfstree = {}
imagepath = []
def pushToList(p):
    list = []
    for item in re.split("\n", p):
        list.append(item)
    return list

def dicTree(l):
    tree = {}
    level = 0
    for index in range(0,len(l)):
        if l[index].count("\t") == 0:
            tree.update({l[index]:"0"})
            level = l[index].count("\t")
        elif l[index].count("\t") > l[index-1].count("\t"):
            tree.update({l[index]:l[index-1]})
        elif l[index].count("\t") == l[index-1].count("\t"):
            tree.update({l[index]:tree.get(l[index-1])})
    return tree

def getParent(child,t):
    return t.get(child)

def popImagePath(l,tr):
    path = []
    for item in l:
        ip = []
        if ".gif" in item or ".jpeg" in item or ".jpg" in item:
            ip.append(item)
            for n in range(0,item.count("\t")):
                ip.append(getParent(ip[n],tr))
            ip.reverse()
            path.append("/"+"/".join(ip).replace("\t","")+"/")
    return path        

dfslist = pushToList(path)
print dfslist
dfstree = dicTree(dfslist)
print dfstree
imagepath = popImagePath(dfslist, dfstree)
print imagepath
#print max(len(item) for item in imagepath)
