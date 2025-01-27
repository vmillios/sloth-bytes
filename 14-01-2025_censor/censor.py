def censor(input: str) -> str:
    output: list[str] = input.split(" ")

    for i in range(len(output)):
        if len(output[i]) >= 5:
            output[i] = "*" * len(output[i])

    return " ".join(output)

print(censor("The code is fourty"))
print(censor("Two plus three is five"))
print(censor("aaaa aaaaa 1234 12345"))