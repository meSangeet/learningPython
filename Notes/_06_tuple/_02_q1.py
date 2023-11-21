#Given a list of non-empty tuples, WAP to get a list, sorted in increasing order by the sun of elements of the tuple. In case of tie, FIFO should be followed


def comp(tp):
    sum = 0
    for i in tp:
        sum += i
    
    return sum, tp[0]


def main():
    lis = [(2,3,1), (1,2,3), (2,3), (2,2)]

    lis.sort(key=comp)

    print(lis)

if __name__ == "__main__":
    main()