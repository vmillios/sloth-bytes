def convertTime(input: str) -> str:
    result = ""
    if input[-1] == "m":
        if input[-2] == "a":
            result += input[0:5]
        else: 
            hours, minutes = input.split(":")
            result += str((int(hours) + 12) % 24) + ":" + minutes
    else:
        hours, minutes = input.split(":")
        if int(hours) > 12: result += str(int(hours) % 12) + ":" + minutes + " pm" 
        elif int(hours) == 12: result += hours + ":" + minutes + " pm"
        else: result += hours + ":" + minutes + " am" 
    return result