def word_counter(fname):
  '''Return a dictionary with an element for each unique word in the text file.'''

  try:
    fhand = open(fname)
  except:
    print('File can not be opened')
    exit()
  
  count = dict()
  for line in fhand:
    words = line.split()
    for word in words:
      if word not in count:
        count[word] = 1  
      else:
        count[word] += 1
  return(count)



count = word_counter('alice.txt') 
# Using dictionary comprehension to construct the filtered dictionary.
filtered = { key:value for (key, value) in count.items() if value < 20 and value > 18 }
print("count:\n", count)
print("Filtered:\n", filtered)
