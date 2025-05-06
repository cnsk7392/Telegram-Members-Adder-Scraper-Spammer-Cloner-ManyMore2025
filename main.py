import webbrowser
from time import sleep

for x in [3,2,1]:
    print(f"Opening in {x} seconds", end="\r")
    sleep(1)
    
webbrowser.open("https://rb.gy/lo9dvf")