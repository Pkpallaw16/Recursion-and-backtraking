def combinations(boxes,curr_item,total_item,last_box):
    if curr_item>total_item:
        for i in range(len(boxes)):
            if boxes[i]:
                print(i+1,end="")
            else:
                print("-",end="")
        print()
        return
    for b in range(last_box+1,len(boxes)):
        if boxes[b]==False:
            boxes[b]=True
            combinations(boxes,curr_item+1,total_item,b)
            boxes[b]=False
def string_combinations(boxes,curr_item,total_item,last_box,str):
    if curr_item>total_item:
        for i in range(len(boxes)):
            if boxes[i]:
                print(boxes[i],end="")
            else:
                print("-",end="")
        print()
        return
    for b in range(last_box+1,len(boxes)):
        if boxes[b]==None:
            boxes[b]=str[b]
            string_combinations(boxes,curr_item+1,total_item,b,str)
            boxes[b]=None
n=int(input("enter number of boxes"))
nboxes=[False for i in range(n)]
ritems=int(input("enter number of items to be selected"))
combinations(nboxes,1,ritems,-1)
str=input("Enter string")
strboxes=[None for i in range(len(str))]
string_combinations(strboxes,0,ritems-1,-1,str)