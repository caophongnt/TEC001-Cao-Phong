def average_score(filename):
    file = open(filename, "r", encoding="utf-8")   
    lines = file.readlines()                       
    file.close()                                   

    total_score = 0
    count = 0

    for line in lines:
        line = line.strip()                        
        if line != "":                            
            parts = line.split(",")               
            name = parts[0]                        
            score = int(parts[1])                 
            total_score = total_score + score
            count = count + 1

    if count > 0:
        average = total_score / count
    else:
        average = 0

    return average


# Chương trình chính
if __name__ == "__main__":
    filename = "Studen.txt" 
    avg = average_score(filename)
    print("Average score of all students:", avg)
