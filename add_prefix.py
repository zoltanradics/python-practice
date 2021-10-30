from concat_string import concat_string

def add_prefix(prefix, target):
  # Check if word is a list
  if not isinstance(target, list):
    # Concatenate prefix and target
    return concat_string(prefix, target)

  # Create list to return
  return_list = []

  # Iterate over target 
  for item in target:
    # Concatenate prefix and target's item
    return_list.append(concat_string(prefix, item))

  # Return list
  return return_list

print(add_prefix('auto', 'gram'))
print(add_prefix('auto', ['gram', 'motive', 'matic']))