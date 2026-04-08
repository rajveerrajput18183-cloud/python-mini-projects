import time
import random 
sentences = [
    "The quick brown fox jumps over the lazy dog.", 
    "Typing speed is a measure of how fast you can type.",
    "Practice makes perfect when it comes to typing.",
    "Accuracy is just as important as speed in typing.",
]
def measure_accuracy(user_input , test_sentence):
    correct_chars = sum(1 for a,b in zip (user_input , test_sentence)if a== b)
    accuracy = (correct_chars / len(test_sentence))*100 if test_sentence else 0
    return accuracy


def typing_test():
    test_sentence = random.choice(sentences)
    print("type the following sentences as fast as you can:")
    print(test_sentence)
    input("press enter to start the test....")
    start_time = time.time() #measure start time 
    user_input = input("\n start typing.. \n")
    end_time = time.time()
    time_taken = end_time - start_time
    words_count=len(user_input.split(" "))




    print("result:")
    print(f"time taken:{time_taken}seconds")
    print(f"words per second:{words_count/(time_taken/60):.2f} words per minute")
    accuracy = measure_accuracy(user_input , test_sentence)
    print(f"accuracy: {accuracy:.2f}%")

typing_test() 