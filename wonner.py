def string_comp (word1, word2):
	word1 = word1.lower()
	word2 = word2.lower()
	if word1[0:2] == word2[0:2]:
		return 0
	elif word1[0] == word2[0] and word1[1] != word2[1]:
		return 1
	elif word1[0] != word2[0] and word1[1] == word2[1]:
		return 2
	else:
		return 3				

print(string_comp("wonner" ,"wnnrt"))