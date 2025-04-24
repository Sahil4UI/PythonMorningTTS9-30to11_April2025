from datetime import datetime
import webbrowser
helloIntent = ["hello","hi","hey","hie","wassup"]
byeIntent = ["bye","tata","see you","ttyl"]
chat = True
while chat ==True:
    msg = input("Enter Msg : ")
    if msg in helloIntent:
        print("hey...")
    elif msg in byeIntent:
        print("Bye...")
        break
    elif "date" in msg:
        dt = datetime.now()
        print(dt.strftime("%d-%m-%Y,%a"))
    elif "time" in msg:
        dt = datetime.now()
        print(dt.strftime("%H:%M:%S,%p"))
    elif "open" in msg:
        webbrowser.open("https://www."+msg.split()[-1]+".com")
    else:
        print("Sorry I dont Understand!!!")

