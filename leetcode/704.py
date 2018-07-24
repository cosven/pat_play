def bs(l, num, base=0):
    length = len(l)
    if length <= 0:
        return -1
    mid = length / 2
    if num == l[mid]:
        return mid + base
    elif l[0] <= num < l[mid]:
        return bs(l[0:mid], num, base=base)
    elif l[-1] >= num > l[mid]:
        return bs(l[mid:], num, base=mid+base)
    return -1


if __name__ == '__main__':
    assert bs([1, 2, 3], 1) == 0
    assert bs([1, 2, 3], 2) == 1
    assert bs([1, 2, 3], 3) == 2

    assert bs([1, 2, 3, 4], 1) == 0
    assert bs([1, 2, 3, 4], 2) == 1
    assert bs([1, 2, 3, 4], 3) == 2
    assert bs([1, 2, 3, 4], 4) == 3

    assert bs([1], 1) == 0
    assert bs([1], 2) == -1

    assert bs([1,2],1) == 0
    assert bs([-1,0,3,5,9,12], 9) == 4
    assert bs([-1,0,3,5,9,12], 12) == 5
