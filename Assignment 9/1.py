def count_lines(filename):
    file = open(filename, "r", encoding="utf-8")  
    lines = file.readlines()                      
    file.close()                                   

    count = 0
    for line in lines:
        if line.strip() != "":                     
            count = count + 1                      
    return count
