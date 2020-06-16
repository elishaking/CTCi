# Time complexity: O(N)
# Space complexity: O(N)
def is_unique(s: str):
    lookup = {}

    for char in s:
        if lookup.get(char):
            return False

        lookup[char] = True

    return True


print(is_unique("uniqe"))
print(is_unique("not unique"))
