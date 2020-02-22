def player(update, read, write)

# This is the part which reads file in
with open('player\player_DEMO') as f:
    for line in f.readlines():
        print (line)

#