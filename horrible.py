
arr = [1,2,3,4,5]
n=5
t = [0]*(2*5) #generating tree
l = [0]*(2*5) #generating corresponding lazy tree
def bui(node,a,b):
    if (a>b) return
    if (a==b):
        t[node]=arr[b]
        return
    bui(node*2,a,(a+b)/2)
    bui(node*2+1,(a+b)/2 +1,b)

    t[node]=t[node*2]+t[node*2+1]


def qu(node,a,b,i,j):
    if a>b or a > j or b < i:
        return 0

    if l[node]!=0:
        t[node]+=l[node]*(b-a+1)
            if a!=b:
                l[node*2]+=l[node]
                l[node*2+1]+=l[node]
        l[node]=0

    if a==i and b===j:
        return t[node]
    
    q1=qu(node*2,a,(a+b)/2,i,j)
    q2=qu(node*2+1,(a+b)/2  +1,b,i,j)
    return q1+q2



if __name__="__main__"

    try:
        t=int(input("Type number of inputs":))
    except ValueError:
        print("This is not a number")
    
    while(t--):
        a=input()
        if a==1:
            p=int(input())
            q=int(input())
        print(q(1,0,n-1,p-1,q-1))
        #push

    

    




    




