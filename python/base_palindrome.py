def isPali(target):
    # expect to get values from deci_to_base, which yields strings
    t = target
    t_1 = list(t)
    t_2 = list(reversed(t_1))
    
    if t_1 == t_2:
        return True
    return False

def deci_to_base(deci_num, base):
    str_rep = []
    while deci_num:
        # append the greatest digit
        str_rep.append(str(deci_num%base))
        # reduce by the base to keep going
        deci_num = deci_num / base
        
    # account for 0, because 0 <= n <= 1000
    if not str_rep:
        return '0'
    return ''.join(str_rep)

def answer(n):
    # your code here
    base = 2
    keep_going = True
    while keep_going:
        str_base_x = deci_to_base(n,base)
        if isPali(str_base_x):
            keep_going = False
            return base
        base += 1

print answer(42)
print answer(0)
print answer(1)
