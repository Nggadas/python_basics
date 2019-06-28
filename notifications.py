def yell(text):
    text = text.upper()
    no_of_chars = len(text)
    result = text + "!" * (no_of_chars // 3)
    print(result)


yell("You are doing great")
yell("Don't forget to ask for help")
yell("Don't repeat yourself, keep things DRY")

