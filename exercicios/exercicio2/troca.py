example = "abc 123"
first_char_1 =example[0:1]
position = int(example.find(" "))
first_char_2 = example[position+1:position+2]

new_first_char_1 = first_char_2
new_first_char_2 = first_char_1

result = new_first_char_1 + example[1:position] + " " + new_first_char_2 + example[position+2:]
print(f"{example}->{result}")