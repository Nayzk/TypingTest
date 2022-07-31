import time



words = "I love programing , data structure and algorithms"

word_count = len(words.split())
print(words)


while True:
    t = time.time()
    text = str(input("Enter the sentence : "))
    t1 = time.time()
    accuracy = len(set(text.split())&set(words.split()))
    type_accuracy = accuracy/word_count
    time_taken = t1 - t
    wpm = word_count/time_taken
    print("WPM", round(wpm, 2))
    print("Accuracy", type_accuracy)
    print("TimeTaken", round(time_taken, 2))


