def tg(prompt="Enter a number {FALLBACK}: "):
    value = "a"
    while value.isalpha():
        proposal = input(prompt)
        if proposal.isalpha():
            print("\nPlease input only a positive number!")
        else:
            value = proposal

    return int(value)