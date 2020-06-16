def get_char(s: str, i: int):
    try:
        return s[i]
    except:
        return None


def one_away(s1: str, s2: str):
    if s1 == s2:
        return True

    i = 0
    j = 0
    diff_count = 0

    while i < len(s1) or j < len(s2):
        if get_char(s1, i) != get_char(s2, j):
            if diff_count == 1:
                return False

            diff_count += 1

            if get_char(s1, i+1) == get_char(s2, j):
                i += 1
            elif get_char(s2, j+1) == get_char(s1, i):
                j += 1

        i += 1
        j += 1

    return diff_count < 2


print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
