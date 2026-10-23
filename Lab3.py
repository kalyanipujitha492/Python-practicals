def main():

seq = [10, 20, 30, 40, 50]

print("Original sequence:", seq)

print("First element:", seq[0])

print("Last element:", seq[-1])

print("Sliced (1:4):", seq[1:4])

print("Is 30 in sequence?", 30 in seq)

print("Length of sequence:", len(seq))

print("Max value:", max(seq))

print("Min value:", min(seq))

if_name__ == '_main__':

main()

Program 2: List Methods

def main():

fruits = ['apple', 'banana', 'cherry'] print("Original list:", fruits)

fruits.append('orange') print("After append:", fruits)

fruits.insert(1, 'mango') print("After insert at index 1:", fruits)

fruits.remove('banana') print("After removing 'banana':", fruits)

fruits.pop() print("After popping last element:", fruits)

fruits.sort() print("After sort:", fruits)

fruits.reverse() print("After reverse:", fruits)

print("Index of mango", fruits.index(mango))

print("Count of apple':", fruits.count(apple))

_name_ _main_

main()

ogram 3: Tuple Methods

Jef main():

tup = (1, 2, 3, 2, 4, 2)

print("Tuple:", tup)

print("Count of 2:", tup.count(2))

print("Index of 4:", tup.index(4))

if_name main() _main_':

Program 4: String Methods

def main():

text = "Hello World"

print("Original text:", text)

print("Lowercase:", text.lower())

print("Uppercase:", text.upper())

print("Replace 'World' with 'Python':", text.replace('World', 'Python'))

print("Find 'World':", text.find('World'))

print("Split:", text.split())

print("Starts with 'H'?", text.startswith('H'))

print("Ends with 'd'?", text.endswith('d'))

if name == '_main_':

main()

Program 5: Built-in Functions on Sequences (enumerate, zip, reversed, sorted)

def main():
  names = ['Alice', 'Bob', 'Charlie']

scores [85, 90, 78]

print("Using enumerate:") for i, name in enumerate(names):

print(f'(i): (name)")

print("\nUsing zip:")

for name, score in zip(names, scores):

print(f"(name) scored (score)")

print("\nReversed names:", list(reversed (names)))

print("Sorted scores:", sorted(scores))

if name == '_main_'

main()
