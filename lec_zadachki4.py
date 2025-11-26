import random
flowers = ["rose", "tulip", "daisy"]
color = ["red", "pink", "white"]

def randomi(color):
    x = random.choice(color)
    return x 

colors = dict(zip(flowers, color))
randomcolor = dict(map(randomi(color), colors))
print(randomcolor)


