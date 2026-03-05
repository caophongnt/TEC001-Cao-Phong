def sum_numbers(paragraph: str):
    current_number = "" 
    total = 0  
    for ch in paragraph:
        if ch.isdigit(): 
            current_number += ch  
        else: 
            if current_number:
                total += int(current_number)  
                current_number = "" 
    if current_number:
        total += int(current_number)   
    return total