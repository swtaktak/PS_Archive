import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

a = int(input().strip())
e = int(input().strip())

if a >= 3 and e <= 4:
    print("TroyMartian")
if a <= 6 and e >= 2:
    print("VladSaturnian")
if a <= 2 and e <= 3:
    print("GraemeMercurian")