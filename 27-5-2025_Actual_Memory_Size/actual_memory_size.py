def actualMemorySize(sizeStr: str) -> str:
    size = float(sizeStr[:-2])
    magnitude = f"{sizeStr[-2]}{sizeStr[-1]}"
    if magnitude == "GB":
        size *= 1000
    ret = size * 0.93
    if ret < 1000:
        return f"{int(ret)}MB"
    else:
        return f"{round(ret/1000, 2)}GB"


print(actualMemorySize("32GB"))
#output = "29.76GB"

print(actualMemorySize("2GB"))
#output = "1.86GB"

print(actualMemorySize("512MB"))
#output = "476MB"