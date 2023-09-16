x = input("Greeting: ").strip()
if x.startswith("hello") or x.startswith("Hello"):
    print("$0")
elif x.startswith("h") or x.startswith("H"):
    print("$20")
else:
    print("$100")