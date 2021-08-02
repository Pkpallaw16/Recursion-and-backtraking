def permutations(curr_box,total_box,items,sel_so_far,total_sel,asf):
    if curr_box>total_box:
        if sel_so_far==total_sel:
            print(asf)
        return
    for i in range(total_sel):
        if items[i]==0:
            items[i]=1
            permutations(curr_box + 1, total_box,items, sel_so_far + 1, total_sel, asf+str(i+1))
            items[i]=0
    permutations(curr_box+1,total_box,items, sel_so_far, total_sel, asf+"0")
def string_permutations(curr_box,total_box,items,sel_so_far,total_sel,asf,str):
    if curr_box>total_box:
        if sel_so_far==total_sel:
            print(asf)
        return
    for i in range(total_sel):
        if items[i]==0:
            items[i]=1
            string_permutations(curr_box + 1, total_box,items, sel_so_far + 1, total_sel, asf+str[curr_box],str)
            items[i] = 0
    string_permutations(curr_box+1,total_box,items, sel_so_far, total_sel, asf,str)

nboxes=int(input("enter number of boxes"))
ritems=int(input(("enter number of items to selected")))
items=[0 for i in range(ritems)]
permutations(1,nboxes,items,0,ritems,"")
str=input("enter string")
string_permutations(0,len(str)-1,items,0,ritems,"",str)