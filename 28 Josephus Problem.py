def josephus_problem(n,k):
    if n==1:
        return 0
    x=josephus_problem(n-1,k)
    y=(x+k)%n
    return y
print(josephus_problem(7,3))