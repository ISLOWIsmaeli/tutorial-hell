narrative=""" 
Welcome to the whimsical world of Madlibs! Prepare to laugh hysterically as you fill in the blanks with nouns, adjectives, and verbs to concoct a delightfully absurd story. First, give me a noun1: ________. Now, an adjective: ________. Followed by another noun2: ________. How about an adverb this time: ________. And finally, a verb ending in 'ing': ________. Now let's unveil the uproarious narrative we've crafted together!
"""
print(narrative)
noun1=input("Enter Noun1: ")
adjective=input("Enter an adjective: ")
noun2=input("Enter noun2: ")
adverb=input("Enter an adverb: ")
verb=input("Enter a verb: ")

noun1.title
noun2.title

print("""Welcome to the whimsical world of Madlibs! Prepare to laugh hysterically as you fill in the blanks with nouns, adjectives, and verbs to concoct a delightfully absurd story. First, give me a noun: {}. Now, an adjective:{}. Followed by another noun: {}. How about an adverb this time: {}. And finally, a verb ending in 'ing': {}. Now let's unveil the uproarious narrative we've crafted together!""".format(noun1,adjective,noun2,adverb,verb))
