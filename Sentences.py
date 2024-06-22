import random





singularNouns = {"bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"}

pluralNouns = {"birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"}

pastVerb = {"drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"}

pressent_plural_Verb = {"drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"}

pressent_singular_verb = {"drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"}

futureVerb = {"will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"}

words_singluar = ["a", "one", "the"]

words_plural = ["some", "many", "the"]

def main():
    quan = input("quantity")
    tense = input("Tense")

    out = make_sentance(quan, tense)

    print(out)


def make_sentance(quantity, tense):

    deter = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)

    out = deter + " " + noun + " " + verb
    return out



def get_determiner(quantity):

    if(quantity == 1):
        return words_singluar[random.randrange(0, len(words_singluar))]
    else:
        return words_plural[random.randrange(0, len(words_plural))]
    


def get_noun(quantity):

    if(quantity == 1):
        out = singularNouns[random.randrange(0, len(singularNouns))]
        return out
    else:
        out = pluralNouns[random.randrange(0, len(pluralNouns))]
        return out
        

def get_verb(quantity, tense):

    if(quantity != 1 ) and (tense == "present"):
        verb = pressent_plural_Verb[random.randrange(0, len(pressent_plural_Verb))]
        return verb
    elif(quantity == 2) and (tense == "present"):
        verb = pressent_singular_verb[random.randrange(0, len(pressent_singular_verb))]
        return verb
    elif(tense == "past"):
        verb = pastVerb[random.randrange(0, len(pastVerb))]
        return verb
    elif(tense == "future"):
        verb = futureVerb[random.randrange(0, len(futureVerb))]
        return verb
    else:
        return None




main()