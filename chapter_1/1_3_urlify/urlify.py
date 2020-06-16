def urlify(s: str):
    return s.strip().replace(" ", "%20")


print(urlify('  this is a url '))
