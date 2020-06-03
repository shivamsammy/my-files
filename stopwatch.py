import time
print(" -- Your stopwatch is ready --")
seconds=int(input(" enter the total number of seconds :"))
for second in range(seconds):
    print(str(seconds-second)+ " seconds remaining")
    time.sleep(1)
print(" TIME IS UP!!")
