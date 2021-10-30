
def concat_string(*args):
  # Define string to return
  return_string = ''

  # Convert any given argument to string and concat them together
  for arg in args:
    return_string += str(arg)
  
  # Return string
  return return_string
