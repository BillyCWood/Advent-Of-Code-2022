def main():

    highest_elf_num = 1 #1 because there is no elf 0

    highest_calories = 0
    second = 0
    third = 0

    current_elf_count = 1
    current_count = 0
    


    f = open("day1a-input.txt", "r")

    for line in f:
        if line == "\n":
            if current_count > highest_calories:
                highest_calories = current_count
                highest_elf_num = current_elf_count
            elif current_count > second and current_count < highest_calories:
                second = current_count
            if current_count > third and current_count < second:
                third = current_count
            current_count = 0
            current_elf_count += 1
        else:
            current_count += int(line)


    f.close()

    print("\nDAY 1a:")
    print(highest_elf_num)
    print(highest_calories)
    print()
    print("DAY 1 b:")
    print(highest_calories+second+third)

main()
