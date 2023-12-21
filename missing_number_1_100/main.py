from chatgpt_answer import find_missing_numbers as chatgpt
from gemini_answer import find_missing_numbers as gemini
from gemini_answer_numpy import find_missing_numbers as gemini_np
from time import perf_counter

arr = [1, 2, 3, 5, 7, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 98, 99]

#Chatgpt
execution_time = []
for _ in range(10):
    t1 = perf_counter()
    chatgpt(arr)
    t2 = perf_counter()
    execution_time.append(t2-t1)

chatgpt_average_time = sum(execution_time)/10

#Gemini
execution_time = []
for _ in range(10):
    t1 = perf_counter()
    gemini(arr)
    t2 = perf_counter()
    execution_time.append(t2-t1)

gemini_average_time = sum(execution_time)/10

#Gemini with numpy
execution_time = []
for _ in range(10):
    t1 = perf_counter()
    gemini_np(arr)
    t2 = perf_counter()
    execution_time.append(t2-t1)

gemini_np_average_time = sum(execution_time)/10

print(chatgpt_average_time)
print(gemini_average_time)
print(gemini_np_average_time)
