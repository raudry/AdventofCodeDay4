#Figure out if there are any overlapping assignment sectins between elves

myFile = open("/Users/dylanworrell/Documents/adventOfCode/elfAssignments.txt","r")

overlaps = 0
for line in myFile:
    assignment = line.rstrip('\n').split(",")
    #Assign sections to first and second elf 
    elf1 = assignment[0].split("-")
    elf1Section1 = elf1[0]
    elf1Section2 = elf1[1]
    elf2 = assignment[1].split("-")
    elf2Section1 = elf2[0]
    elf2Section2 = elf2[1]

    #if the first section of elf1 is less than the first section of elf2
    #and the last section of elf1 is greater than the second section of elf2
    #then it overlaps
    #or
    ##if the first section of elf2 is less than the first section of elf1
    #and the last section of elf2 is greater than the second section of elf1
    #then it overlaps
    if (elf1Section1 <= elf2Section1 and elf1Section2 >= elf2Section2) or (elf2Section1 <= elf1Section1 and elf2Section2 >= elf1Section2):
        overlaps += 1

        
print(overlaps)


