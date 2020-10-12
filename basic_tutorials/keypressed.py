import readchar

while True:
    print "\nPress 'A' to Start the recording"
    print "      'Z' to Stop the recording"
    print "      'Enter' to quit the program..."

    # Read a key
    key = readchar.readkey()
    if(key == 'A'):
        print "Started Recording..."
    elif(key == 'Z'):
        print "Stopped Recording..."
    elif(key == '\r'):
        print "Exiting..."
        break
    else:
        print "Please Use only allowed keys: A, Z, Enter!" 

