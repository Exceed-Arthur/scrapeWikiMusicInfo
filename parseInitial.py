import initialGrabber
from nonsense import nonsense
ideas = initialGrabber.ideas
prepositions = ["you", "of", "and", "with", "your", "my", "if", "is", "to", "a", "for", "I", "i", "we", "We", "N'", "n'", "What's", "what's", "i'm", "'round", "i've", "in", "oh", "of", "but", "all", "we", "i'll", "you're", "that's", "let's", "where", "in"]
for idea in ideas:
    for nonsensicals in nonsense:
        if nonsensicals in idea[1].lower() or idea[1].lower() in prepositions:
            print(idea[1])
            # print(f"NONSENSE FOUND AT {nonsensicals}")
            ideas.remove(idea)

for idea in ideas:
    print(f"{idea[0]}: {idea[1]}")


print(len(ideas))