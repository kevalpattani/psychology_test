import questionst as ques
import json
import test
import datetime


def main():
    print("Welcome to the psychology test")
    phq_test = ques.phq9
    phq_data = test.load_data(phq_test)
    result_phq = test.evaluate_data(phq_test,phq_data)
    print(result_phq)
    print("----------------")
    print("----------------")

    
    phy_test = ques.physical_health_ques
    phy_data = test.load_data(phy_test)
    result_pyh = test.evaluate_data(phy_test,phy_data)
    print("----------------")
    print("----------------")
    t = 0

    if phq_data < 10 and phy_data < 4:
        ques_12 = ques.ghq_12_questions_awell
        ques_12_data = test.load_data(ques_12)
        ques_12_result = test.evaluate_data(ques_12,ques_12_data)
        print("test ends here you data will be stored in a json file")
        t = 1

    if phq_data >= 10 and phy_data >= 4:
        ques_28 = ques.ghq_28_questions_gemini
        ques_28_data = test.load_data(ques_28)
        ques_28_result = test.evaluate_data(ques_28,ques_28_data)
        print("test ends here you data will be stored in a json file")
        t = 2

    today = datetime.date.today()
    current_time = datetime.datetime.now().time()
    timestamp = datetime.datetime.combine(today, current_time)
    timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")


    if t == 1:
        data = {
            "psychological_num" : phq_data,
            "psychological_condition" : result_phq,
            "physical_num" : phy_data,
            "physical_result" : result_pyh,
            "12_psychological_que_num" : ques_12_data,
            "12_psychological_result" : ques_12_result,
            # "28_questions_num" : ques_28_data,
            # "28_questions_condition" : ques_28_result,
            "timestamp": timestamp_str
        }

    if t == 2:
        data = {
            "psychological_num" : phq_data,
            "psychological_condition" : result_phq,
            "physical_num" : phy_data,
            "physical_result" : result_pyh,
            # "12_psychological_que_num" : ques_12_data,
            # "12_psychological_result" : ques_12_result,
            "28_questions_num" : ques_28_data,
            "28_questions_condition" : ques_28_result,
            "timestamp": timestamp_str
        }

    if t == 0:
        data = {
            "psychological_num" : phq_data,
            "psychological_condition" : result_phq,
            "physical_num" : phy_data,
            "physical_result" : result_pyh,
            # "12_psychological_que_num" : ques_12_data,
            # "12_psychological_result" : ques_12_result,
            # "28_questions_num" : ques_28_data,
            # "28_questions_condition" : ques_28_result,
            "timestamp": timestamp_str
        }

    new_data = "\n" + str(data)
    with open("results.txt", "a") as file:
        file.write(new_data)
    file.close()

if __name__ == "__main__":
    main()