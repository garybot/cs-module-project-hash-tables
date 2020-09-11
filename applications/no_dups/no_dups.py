# def no_dups(s):
#     arr = set(s.split())
#     return len(" ".join(arr))

def no_dups(s):
	new_string = ""
	word = ""
	words = {}

	for char in s: #n
		if char != " ": #1
			word += char #1
		else:
			if not words.get(word): #1
				if len(new_string): #1
					new_string += " " #1
				words[word] = True #1
				new_string += word #1

			word = "" #1

	if not words.get(word): #1
		new_string += word #1 

	return len(new_string)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))