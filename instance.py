from Bird import *
print('\nClass Instances Of:\n', Bird.__doc__)

polly = Bird('Squawk, squawk!')

print('\nNumber of Birds: ', Bird.count)
print('Polly Says:', polly.talk())

harry = Bird('Tweet, tweet!')
print('\nNumber of Birds: ', Bird.count)
print('Harry Says: ', harry.talk())