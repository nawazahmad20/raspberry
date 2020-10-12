# Find the right getch() and getKey() implementations
try:
    # POSIX system: Create and return a getch that manipulates the tty
    import termios
    import sys, tty
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

    # Read arrow keys correctly
    def getKey():
        firstChar = getch()
        if firstChar == '\x1b':
            return {"[A": "up", "[B": "down", "[C": "right", "[D": "left"}[getch() + getch()]
        else:
            return firstChar

except ImportError:
    # Non-POSIX: Return msvcrt's (Windows') getch
    from msvcrt import getch

    # Read arrow keys correctly
    def getKey():
        firstChar = getch()
        if firstChar == b'\xe0':
            return {"H": "up", "P": "down", "M": "right", "K": "left"}[getch()]
        else:
            return firstChar
