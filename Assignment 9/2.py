def find_keyword_lines(filename, keyword):
    file = open(filename, "r", encoding="utf-8") 
    lines = file.readlines()                       
    file.close()                                

    result = []                                   
    line_number = 1                                

    for line in lines:
        if keyword in line:                       
            result.append(line_number)            
        line_number = line_number + 1             

    return result
