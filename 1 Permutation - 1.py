def permutations(boxes,curr_item,total_item):
    if curr_item>total_item:
        print(boxes)
        return

    for i in range(len(boxes)):
        if boxes[i]==0:
            boxes[i]=curr_item
            permutations(boxes,curr_item+1,total_item)
            boxes[i]=0

def string_permutation(places,curr_pos,total_pos,str):
    if curr_pos>total_pos:
        print("".join(places))
        return
    for i in range(len(places)):
        if places[i]==0:
            places[i]=str[curr_pos]
            string_permutation(places,curr_pos+1,total_pos,str)
            places[i]=0
    

n_boexs=int(input("enter number of boxes"))
boxes=[0 for i in range(n_boexs)]
places=[0 for i in range(3)]
ritems=int(input("enter items to be selected"))
permutations(boxes,1,ritems)
string_permutation(places,0,2,"abc")