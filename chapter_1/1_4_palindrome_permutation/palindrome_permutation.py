# Time complexity: ~ O(N)
# Space complexity: O(N)
def palindrom_permutation(s: str):
    s = s.strip().lower().replace(' ', '')
    lookup = {}

    for char in s:
        if lookup.get(char):
            lookup[char] += 1
        else:
            lookup[char] = 1

    one_odd = False
    for char_count in lookup.values():
        if char_count % 2 != 0:
            if one_odd:
                return False
            else:
                one_odd = True

    return True


print(palindrom_permutation("lelve"))
print(palindrom_permutation("Tact Coa"))
