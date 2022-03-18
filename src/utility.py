import main


def printDebug(Value):  # Enabled when global debug mode is on
    if main.DEBUG_MODE == 1:
        print(Value)
