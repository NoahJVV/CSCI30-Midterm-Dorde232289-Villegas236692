capacity = 5
out = []
for i in range(10):
    out.insert(0,i)
    if(len(out) > capacity): out.pop(capacity)
    print(out)