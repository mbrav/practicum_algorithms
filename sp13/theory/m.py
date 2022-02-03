# 64788113

def in_put(string: str = None):
    def str_or_inputs(st: str):
        st = st.split(' ')
        # if len(st) > 1:
        return list(map(lambda x: int(x), st))
        # return int(st[0])
    if string:
        return str_or_inputs(string)
    return str_or_inputs(input())


def get_k(nums1, start1, end1, nums2, start2, end2, k):
    len1 = end1 - start1 + 1
    len2 = end2 - start2 + 1
    if (len1 > len2):
        return get_k(nums2, start2, end2, nums1, start1, end1, k)
    if (len1 == 0):
        return nums2[start2 + k - 1]
    if (k == 1):
        return min(nums1[start1], nums2[start2])
    i = start1 + min(len1, k // 2) - 1
    j = start2 + min(len2, k // 2) - 1
    if (nums1[i] > nums2[j]):
        return get_k(
            nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
    else:
        return get_k(
            nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))


def get_median(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    length = n + m
    k_pre = (length + 1) // 2
    k = (length + 2) // 2
    if (length % 2 == 0):
        out = (get_k(nums1, 0, n - 1, nums2, 0, m - 1, k_pre) +
               get_k(nums1, 0, n - 1, nums2, 0, m - 1, k)) * 0.5
        if str(out)[-1] == '0' and str(out)[-2] == '.':
            return int(out)
        return out
    else:
        return get_k(nums1, 0, n - 1, nums2, 0, m - 1, k)


def main():
    n = in_put()
    n2 = in_put()
    arr1 = in_put()
    arr2 = in_put()

    # m = in_put('8')
    # n = in_put('10')
    # arr1 = in_put('0 0 0 1 3 3 5 10')
    # arr2 = in_put('4 4 5 7 7 7 8 9 9 10')

    print(get_median(arr1, arr2))


if __name__ == "__main__":
    main()
