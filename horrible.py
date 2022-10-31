n, q = map(int, input().split())
arr = [int(x) for x in input().split()] 
size = 3*n
tree=[]
treeAdd=[]
mulTree=[]
for i in range(size):
    tree.append(0)
    treeAdd.append(0)
    mulTree.append(1)
mod = 10 ** 9 + 7
def build(pos = 0, l = 0 ,r = n-1):
    if l == r:
       tree[pos] = arr[l] 
    else:
       mid = (l+r)//2
       build(pos*2+1, l, mid)
       build(pos*2+2, mid+1, r) 
       tree[pos] = (tree[pos*2+1] + tree[pos*2+2]) % mod
       
def lazyPush(pos, l, r):
    tree[pos] *= mulTree[pos]
    tree[pos] += treeAdd[pos] * (r-l+1)
    tree[pos] %= mod 
    if l < r:
        mulTree[pos*2+1] *= mulTree[pos] 
        mulTree[pos*2+2] *= mulTree[pos] 
        treeAdd[pos*2+1] *= mulTree[pos] 
        treeAdd[pos*2+2] *= mulTree[pos] 
        treeAdd[pos*2+1] += treeAdd[pos] 
        treeAdd[pos*2+2] += treeAdd[pos] 
    mulTree[pos] = 1 
    treeAdd[pos] = 0 
    
def update(type,pos , l , r, start, end , val):
    lazyPush(pos, l, r)
    if l > end or r < start : return 
       
    if start <= l and r <= end:
        if type == 1:
           treeAdd[pos] += val 
        elif type == 2:
           mulTree[pos] *= val 
           treeAdd[pos] *= val 
        else:
           mulTree[pos] = 0 
           treeAdd[pos] = val 
        lazyPush(pos, l, r) 
    else:
        mid = (l+r)//2
        update(pos*2+1, l, mid, start, end, type, val) 
        update(pos*2+2, mid+1, r, start, end, type, val) 
       
        tree[pos] = (tree[pos*2+1] + tree[pos*2+2]) 
        
def query(pos, l, r , start , end):
    lazyPush(pos, l, r) 
    
    if l > end or r < start :
      
        return 0 
    if  start <= l and r <= end:
        
        return tree[pos] 
    mid = (l + r) // 2
    return (query(pos*2+1, l, mid, start, end) + query(pos*2+2, mid+1, r, start, end)) 
    
build()

while q:
    quarr=[int(x) for x in input().split()] 
    q=q-1
    if quarr[0]==4:
        print(query(0,0,len(arr)-1,quarr[1],quarr[2])%mod)
    else:
        update(quarr[0],0,0,len(arr)-1,quarr[1],quarr[2],quarr[3])

        
    
           
        
        
        
        
       
