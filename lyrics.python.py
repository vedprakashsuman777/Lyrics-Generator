import requests
import numpy as np
response = requests.get("https://raw.githubusercontent.com/coding-blocks-archives/ML-Noida-2019-June-Two/master/datasets/speeches/speech.txt")
data = response.text
print(data[:1000])
"""
Markov Chains

# text = "the man was .... they then ... the ... the .."

# X =( input), y = output

#(k= 3)
X.      y.       freq
the    _          3
the    y          1
the    n          1
"""
def generatetable(data, k = 4):
  T = {}

  for i in range(len(data)-k):
    X = data[i:i+k]
    y = data[i+k]

    if T.get(X) is None:
      T[X] = {}
      T[X][y] = 1
    else:
      if T[X].get(y) is None:
        T[X][y] = 1
      else:
        T[X][y] +=1

  return T

d = "hello helli hello helly helli hello hello"
generatetable(d, k=4)
T = generatetable(data.lower(), k = 4)
possible_chars = list(T['ear '].keys())
possible_values = list(T['ear '].values())
sum_ = sum(T['ear '].values())
probabs =  np.array(possible_values)/sum_
print(probabs)
np.random.choice(possible_chars, p = probabs)
inital_content = "dear country"
k = 4

for i in range(1000):
  inp = inital_content[-k:]

  possible_chars = list(T[inp].keys())
  possible_values = list(T[inp].values())

  sum_ = sum(T[inp].values())

  probabs =  np.array(possible_values)/sum_

  next_char = np.random.choice(possible_chars, p = probabs)

  inital_content += next_char

print(inital_content)


# sampling
l = ["apple", "mango", "banana"]

for i in range(10):
  e = np.random.choice(l, p =[0.6, 0.3, 0.1] )
  print(e)



