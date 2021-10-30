def remove_suffix(word, suffix):
	# Get out base of the world without the suffix
	base = word.removesuffix(suffix)
	# Get last character of base
	base_last_character = base[len(base)-1] # i
	# Get base without its last character
	base_without_last_character = base[0:len(base)-1] # happ

	# if last character equals to i
	if base_last_character == 'i': 
		# Return base without last character + y
		return  base_without_last_character + 'y' 
	else:
		# Simply return the base
		return base