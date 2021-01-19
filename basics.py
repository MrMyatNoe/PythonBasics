def sentence_maker(phrase):
    interrogatives = ('why','how','what','where','who','when')
    greetings = ('hi','hello','oh','yeah','yes','got it','hey','dude')
    captialized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(captialized)
    elif phrase.startswith(greetings):
        return "{}!".format(captialized)
    else:
        return "{}.".format(captialized)

result = []
while True:
    user_input = input("Say Something : ")
    if user_input == "/end":
        break
    else:
        result.append(sentence_maker(user_input))

print(" ".join(result))