def load_data(dict):
    point = 0
    count = 0
    iterations = 0
    for i,question in enumerate(dict.values(), 1):
        if question != "--":
            while True:
                try:
                    answer = int(input(f"{i}. {question}: "))
                    if 0 <= answer <= 3:
                        if 2 <= answer <= 3:
                            point += answer
                        if answer == 1:
                            count += 1
                            if count > 5:
                                point += 1
                        break
                    else:
                        print("Please enter a valid value between 0 and 3.")
                except:
                    print("Invalid input. Please enter a number.")
        else:
            break
    return point
                    
result_in = 0
def evaluate_data(dict,result):
    global result_in
    for i,question in enumerate(dict.values(), 1):
        for k,v in dict.items():
            if k == "score":
                score_check = v.split(".")
            if k == "range":
                    range_check = v.split(".")
    for i in range(0,len(score_check)):
        if int(score_check[i]) < result:
            continue
        else:
            result_in = i
            range_of_p = range_check[i]
            return range_of_p
            break
    