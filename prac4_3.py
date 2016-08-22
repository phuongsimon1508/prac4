def main():
    numbers= []
    for i in range(5):
        num = int(input(" please put your number : "))
        numbers.append(num)

    print(" the firs number is {}".format(numbers[0]))
    print (" the last number is {}".format(numbers[-1]))
    print("the smallesr number is {}".format(min(numbers)))


main()