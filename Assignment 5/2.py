def b(s: str):
    if len(s) > 7:
        return False
    for ch in s:
        if s[0] != '#':
            return False
        if ch < 'A' or ch > 'Z':
            return False
        if ch < '0' or ch > '9':
            return False
        if ch < 'a' or ch > 'z':
            return False
    return True
   