def interactive_gen():
    print("Generator started")

    msg = yield "Ready"

    print(f"Received: {msg}")
    yield "Done"

g = interactive_gen()

print(next(g))  

print(g.send("Aayush Raj Giri"))       