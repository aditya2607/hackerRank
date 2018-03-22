#wrote in python 2

w1 = raw_input()
w2 = raw_input()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    total += w1.count(letter) if (letter in w1 and letter not in w2) else 0 + w2.count(letter) if (letter not in w1 and letter in w2) else 0 + (w1.count(letter)-w2.count(letter)) if (w1.count(letter) > w2.count(letter)) else (w2.count(letter)-w1.count(letter))
print total
