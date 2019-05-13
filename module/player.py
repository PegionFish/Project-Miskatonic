'''
In my project, this player module should take care of all things that effects PC by adding or cutting points from their cards.
When the game starts, this module should be automaticlly called for reading PC data from file(located at player folder).
Read it up and automaticlly generate dict with data needed. Now I've completed how to read-in in 13th May 2019, I need to solve how to generate dicts and how to format the data.
'''
def player(update, read, write)

# This is the part which reads file in
with open('player\player_DEMO') as f:
    for line in f.readlines():
        print (line)

#