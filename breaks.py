import time
import webbrowser

count = 0
print "This program starts at "+ time.ctime()
while(count < 3):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=DZn5VjLiJ7s&list=RDDZn5VjLiJ7s")
    count = count + 1

print "Good Bye"
