n = input("code: ")
result = [w.lower() for w in reversed(n.split()) if w[0].isupper()]
print('says:',' '.join(result))