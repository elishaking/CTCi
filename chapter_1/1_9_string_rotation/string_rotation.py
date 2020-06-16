def string_rotation(s1: str, s2: str):
    if len(s1) != len(s2):
        return False

    joined = s1 + s1
    if joined.find(s2) == -1:
        return False

    return True


print(string_rotation('waterbottle', 'erbottlewat'))
