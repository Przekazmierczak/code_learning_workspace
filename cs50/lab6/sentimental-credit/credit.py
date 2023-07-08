# TODO
while True:
    inputNumber = input('Card number: ')
    number = inputNumber
    if number.isnumeric() is True:
        if len(number) == 13 or len(number) == 15 or len(number) == 16:
            break

inputNumber = int(inputNumber)
number = int(number)

counter = 0
oddSum = 0
evenSum = 0

#Loop checking card correction
while (number != 0):
    digit = number % 10
    number = number // 10
    counter += 1
    if (counter % 2 == 1):
        oddSum = oddSum + digit
    else:
        evenDigit = digit * 2
        if evenDigit >= 10:
            evenSum = evenSum + (evenDigit % 10) + (evenDigit // 10)
        else:
            evenSum = evenSum + evenDigit

cardCorrection = oddSum + evenSum

amexTest = pow(10, (counter - 2))
mastercardTest = pow(10, (counter -2))
visaTest = pow(10, (counter - 1))

#American Express
if (cardCorrection % 10 == 0 and counter == 15 and (inputNumber // amexTest == 37 or inputNumber // amexTest == 34)):
    print('Amex')
elif (cardCorrection % 10 == 0 and counter == 16 and (inputNumber // mastercardTest == 51 or inputNumber // mastercardTest == 52 or inputNumber // mastercardTest == 53 or inputNumber // mastercardTest == 54 or inputNumber // mastercardTest == 55)):
    print('MASTERCARD')
elif (cardCorrection % 10 == 0 and (counter == 13 or counter == 16) and inputNumber // visaTest == 4):
    print('VISA')
else:
    print('INVALID')