from classes import DEBUG_MODE


def printDebug(Value):  # Enabled when global debug mode is on
    if DEBUG_MODE == 1:
        print(Value)
