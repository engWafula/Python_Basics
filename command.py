cmd = ""
started = False
stopped = False
while True:
   cmd = input(">").lower()
   if cmd == "start":
       if started:
           print("Car already started")
       else:
           started =True
           print("Starting..")
   elif cmd == "stop":
       if not started:
           print("Car already stopped")
       else:
           started = False
           print("Stoping...")
   elif cmd == "help":
       print("""
start - to start the car
stop  - to stop the car
quit  - quit
       """)
   elif cmd == "quit":
       break
   else:
       print("Sorry I do not understand that")
