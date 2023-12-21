from chatgpt_answer import find_pairs as chatgpt
from gemini_answer import two_sum as gemini
from time import perf_counter

target = 26
arr = [23, 7, 0, 15, 19, 14, 23, 2, 30, 5, 20, 26, 21, 27, 15, 0, 24, 1, 4, 19, 6, 18, 27, 16, 26, 1, 8, 20, 0, 12, 3, 16, 21, 1, 11, 7, 18, 7, 16, 12, 19, 1, 12, 17, 16, 16, 28, 2, 23, 16]




#Chatgpt
execution_time = []
for _ in range(10):
    t1 = perf_counter()
    chatgpt(arr,target)
    t2 = perf_counter()
    execution_time.append(t2-t1)

chatgpt_average_time = sum(execution_time)/10



#Gemini
execution_time = []
for _ in range(10):
    t1 = perf_counter()
    gemini(arr,target)
    t2 = perf_counter()
    execution_time.append(t2-t1)

gemini_average_time = sum(execution_time)/10



print(chatgpt_average_time)
print(gemini_average_time)
