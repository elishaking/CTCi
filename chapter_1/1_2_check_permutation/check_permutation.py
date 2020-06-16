def char_sum(s: str):
    sum = 0
    for char in s:
        sum += ord(char)

    return sum


# Time complexity: O(M+N)
# Space complexity: O(1)
def check_permutation(s1: str, s2: str):
    sum1 = char_sum(s1)
    sum2 = char_sum(s2)

    if sum1 == sum2:
        return True

    return False


print(check_permutation("same", "same"))
print(check_permutation("same", "smae"))
print(check_permutation("same", "not same"))
