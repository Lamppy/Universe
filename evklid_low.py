def gcd_mod(num_1, num_2):
    num_first = num_1
    num_second = num_2
    while num_first!= num_second:
        if num_first>=num_second:
            num_first -=num_second
        else:
            num_second -= num_first
    return num_first or num_second
if __name__=='__main__':
    num_1=int(input())
    num_2=int(input())
    print(gcd_mod(num_1, num_2))
