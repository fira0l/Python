sentence = "What is the Airspeed Velocity of an unladen Swallow?"

word_list = [word for word in sentence.split()]
result = {word: len(word) for word in word_list}

print(result)