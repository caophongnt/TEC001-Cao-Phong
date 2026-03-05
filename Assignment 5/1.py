def a(s: str):
    if len(s) < 5 or len(s) > 6: 
        return False
    letters = s[:-3]
    digits = s[-3:]
    if len(letters) < 2 or len(letters) > 3:
        return False
    for ch in letters:
        if ch < 'A' or ch > 'Z':
            return False
    for ch in digits:
        if ch < '0' or ch > '9':
            return False
    return True

#mẫu để chạy thử xem cái function ở trên có chuẩn ko :))
if __name__ == "__main__":
    a = ["TEC001", "AU006", "CS101", "tec001", "T001", "AB1234"]
    for code in a:
        if a(code):
            print(code, "-> đúng")
        else:
            print(code, "-> sai")