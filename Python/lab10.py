
print("=" * 40)
print("         TEXT PROCESSING TOOL")
print("=" * 40)

sentence = input("Enter a sentence: ")

print()
print("--- Processing Results ---")

pos = int(input("Enter position for indexing: "))
print("Character at position", pos, " :", repr(sentence[pos]))

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
print("Sliced string [" + str(start) + ":" + str(end) + "]       :", repr(sentence[start:end]))

print("Uppercase                      :", sentence.upper())
print("Lowercase                      :", sentence.lower())

old_word = input("Enter word to replace         : ")
new_word = input("Enter replacement word        : ")
print("After replace                  :", sentence.replace(old_word, new_word))

print("Length of sentence             :", len(sentence))

print()
print("=" * 40)
print("Analysis Complete!")
print("=" * 40)