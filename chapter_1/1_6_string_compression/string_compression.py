# Time complexity: O(N)
# Space complexity: O(1) or O(N) if we think of a string as an array of characters
def string_compression(s: str):
    new_str = ''
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            new_str += s[i-1] + str(count)
            print(s[i-1] + str(count))
            count = 1

    new_str += s[len(s) - 1] + str(count)

    if len(new_str) >= len(s):
        return s

    return new_str


print(string_compression("ddsss"))
