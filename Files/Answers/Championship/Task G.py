l1, w1, h1 = map(int, input().split())
l1, w1 = max(l1, w1), min(l1, w1)
l2, w2, h2 = map(int, input().split())
l2, w2 = max(l2, w2), min(l2, w2)
lc, wc, hc = map(int, input().split())
lc, wc = max(lc, wc), min(lc, wc)
if h1 + h2 <= hc and l1 <= lc and w1 <= wc and l2 <= lc and w2 <= wc:
    print("YES")
elif l1 <= lc and w1 <= wc and l2 <= lc and w2 <= wc and h1 <= hc and h2 <= hc:
    if l1 <= lc and w1 <= wc:
        if (l2 <= wc - w1 and w2 <= lc) or (w2 <= wc - w1 and l2 <= lc) or (l2 <= lc - l1 and w2 <= wc) or (
                w2 <= lc - l1 and l2 <= wc):
            print("YES")
        elif w1 <= lc and l1 <= wc:
            if (l2 <= wc - l1 and w2 <= lc) or (l2 <= lc and w2 <= wc - l1) or (l2 <= lc - w1 and w2 <= wc) or (
                    w2 <= lc - w1 and l2 <= wc):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
