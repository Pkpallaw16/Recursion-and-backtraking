def combinations(curr_box,total_box,sel_so_far,total_sel,asf):
    if curr_box>total_box:
        if sel_so_far==total_sel:
            print(asf)
        return
    combinations(curr_box + 1, total_box, sel_so_far + 1, total_sel, asf+"i")
    combinations(curr_box+1,total_box, sel_so_far, total_sel, asf+"-")
def string_combinations(curr_box,total_box,sel_so_far,total_sel,asf,str):
    if curr_box>total_box:
        if sel_so_far==total_sel:
            print(asf)
        return
    string_combinations(curr_box + 1, total_box, sel_so_far + 1, total_sel, asf+str[curr_box],str)
    string_combinations(curr_box+1,total_box, sel_so_far, total_sel, asf,str)

nboxes=int(input("enter number of boxes"))
ritems=int(input(("enter number of items to selected")))
combinations(1,nboxes,0,ritems,"")
str=input("enter string")
string_combinations(0,len(str)-1,0,ritems,"",str)