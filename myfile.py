import pandas as pd
screen_time = [5,4,3,2,1]
stu_name = ["varun","sharma","trishanth","reddy","lite take"]
id = [1,2,3,4,5]
dict1 = {"screen_time": screen_time, "stu_name":stu_name,"id":id}
df = pd.DataFrame(dict1)
print(dict1)