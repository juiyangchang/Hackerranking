from collections import defaultdict
import sys

line_count = 0       
lookup = {0:0}
takeaway = [5, 2, 1]

for line in sys.stdin:
    if line_count == 0:
        T = int(line.strip())
    elif line_count % 2 == 1:
        N = int(line.strip())        
    else:
        chocolates = sorted(list(map(int, line.strip().split())))
        if N != len(chocolates):
            print(0)
        else:
            res = []
            for base in range(3):
                operations = 0
                for c in chocolates:
                    diff = c - chocolates[0] + base
                    
                    if diff in lookup:
                        operations += lookup[diff]
                    else:
                        op = 0
                        orig_diff = diff
                        for e in takeaway:
                            while diff - e >= 0:
                                quotient, diff = diff // e, diff % e
                                op += quotient
                                if diff in lookup:
                                    op += lookup[diff]
                                    diff = 0
                        lookup[orig_diff] = op
                        operations += lookup[orig_diff]
                res.append(operations)
            print(min(res))          
    line_count += 1 