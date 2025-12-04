





def solve1():
    digits = []
    with open("input.txt") as f:
        sum = 0   
        for line in f.readlines():
            #ignore last digit
            digits.append([int(x) for x in line.strip()])
            
            #find the highest digit and split there
            max_digit = max(digits[-1][:-1])
            index = digits[-1].index(max_digit)
            first_half = digits[-1][:index+1]
            second_half = digits[-1][index+1:]

            #get highest digit from each half
            max_first = max(first_half) 
            max_second = max(second_half) 
            highest_digits_str = str(max_first) + str(max_second)
            sum += int(highest_digits_str)
    print(sum)

def solve2():
    digits = []
    with open("input.txt") as f:
        sum = 0   
        for line in f.readlines():
            digits.append([int(x) for x in line.strip()])
           
      
    print(sum)
solve1()