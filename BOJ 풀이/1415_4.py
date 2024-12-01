import sys
input = sys.stdin.readline

names = str(input().rstrip())

if '(' in names:
    open_idx = names.index("(")
    main_name = names[0:open_idx-1]
    sub_name = names[open_idx+1:-1]
    
    print(main_name)
    print(sub_name)

else:
    print(names)
    print('-')