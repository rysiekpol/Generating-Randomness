import random

#print("Please give AI some data to learn...")
data = ""
triad = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0]
    , "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}
print("Print a random string containing 0 or 1:")
joined_list = ''.join([x for x in list(input()) if x in '01'])
data += joined_list
while len(data) < 100:
    print("The current data length is " + str(len(data)) + ", " + str(100 - len(data)) + " symbols left")
    print("Print a random string containing 0 or 1:")
    joined_list = ''.join([x for x in list(input()) if x in '01'])
    data += joined_list
print("Final data string:")
print(data)

for x in range(len(data) - 3):
    triad_joined = data[x] + data[x + 1] + data[x + 2]
    value = triad.get(triad_joined)
    value[int(data[x + 3])] += 1

# print(''.join(f"\n{key}: {triad[key][0]},{triad[key][1]}" for key in triad))
print("You have $1000. Every time the system successfully predicts your next press, you lose $1. Otherwise, "
      "you earn $1. Print \"enough\" to leave the game. Let's go!")

balance = 1000

while True:
    print("Print a random string containing 0 or 1:")
    test_string = input()
    if test_string == "enough":
        print("Game over!")
        exit(0)
    test_string = ''.join([x for x in list(test_string) if x in '01'])
    if(len(test_string) > 3):
        predicted_string = ""
        for i in range(3):
            predicted_string += str(random.randint(0, 1))

        current_position = 4
        for i in range(len(test_string) - 3):
            triad_joined = ''.join("%s" % ''.join(map(str, test_string[x])) for x in range(i, i + 3))
            if triad.get(triad_joined)[0] > triad.get(triad_joined)[1]:
                predicted_string += "0"
            else:
                predicted_string += "1"

        print("prediction:\n", predicted_string, sep="")
        how_many_right = sum([1 if predicted_string[x] == test_string[x] else 0 for x in range(3, len(test_string))])
        right_percentage = round(how_many_right * 100 / (len(test_string) - 3), 2)
        print(f'Computer guessed right {how_many_right} out of {len(test_string) - 3} symbols ({right_percentage}%)')
        balance = balance - 2*how_many_right + len(test_string) - 3
        print(f"Your balance is now ${balance}")

        for i in range(len(test_string) - 3):
            triad_joined = ''.join("%s" % ''.join(map(str, test_string[x])) for x in range(i, i + 3))
            triad.get(triad_joined)[int(data[i + 3])] += 1