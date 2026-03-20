def truncateSentence(s, k):
    words = s.split()      
    return " ".join(words[:k])
s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s, k))