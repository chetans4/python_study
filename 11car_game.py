#Car Game
started = False
while True:
    command = input("> ")
    if command.upper() == "START":
        if started:
            print ("Car already started")
        else:
            print ("Car started...")
            started = True
    elif command.upper() == 'STOP':
        if not started:
            print ("Car already stopped")
        else:
            print ("Car stopped...")
            started = False
    elif command.upper() == 'HELP':
        print ("""START- Run the task\nSTOP - Stop the car
QUITE - Quite the game""")
    elif command.upper() == 'QUITE':
        break
    else:
        print ("I do not understand that")
        
        