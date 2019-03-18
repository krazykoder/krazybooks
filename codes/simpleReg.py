"""
Change the values of training & test data set for different output
"""

training_data_set = [[2,1500],[3,2800],[5,4200],[13,6400],[8,5000],[16,9000],[11,5800],[14,8400],[10,5300]]

test_data_set = [9,4,6,1,7,15]

def train(data_set):
    x = 0
    y = 0
    xy = 0
    xx = 0
    length_of_data = len(data_set)
    
    for i in range(length_of_data):
        x += data_set[i][0]
        y += data_set[i][1]
        xy += data_set[i][0] * data_set[i][1]
        xx += data_set[i][0] * data_set[i][0]
        
    x_a = x/length_of_data
    y_a = y/length_of_data
    xy_a = xy/length_of_data
    xx_a = xx/length_of_data
    
    a = (xy_a - x_a*y_a)/(xx_a - x_a*x_a)
    b = (y_a - a*x_a)
    
    def h(X):
        return a*X + b
        
    return h
    
target_func = train(training_data_set)


print_text = "  Input:\n\n"+" "*10+"Training Data Set\n"+" "*3+"_"*30+"\n"+" "*2+"|"+" "*3+"Years of"+" "*4+"|"+" "*4+"Salary"+" "*4+"|\n  |  Experience   |   (in USD)   |\n  |"+"-"*30+"|\n"

for i in range(len(training_data_set )):
    print_text += "  |"+" "*(9-len(str(training_data_set[i][0])))+str(training_data_set[i][0])+" "*6+"|"+" "*(9-len(str(training_data_set[i][1])))+str(training_data_set[i][1])+" "*5+"|\n"


print_text += "  |"+"_"*30+"|"+"\n"*3

print_text += "  Output:\n\n"+" "*12+"Test Results\n"+" "*3+"_"*30+"\n"+" "*2+"|"+" "*3+"Years of"+" "*4+"|"+" "*2+"Estimated"+" "*3+"|\n  |  Experience   |  (Salary)    |\n  |"+"-"*30+"|\n"

for i in range(len(test_data_set)):
    est_sal = str(format(target_func(test_data_set[i]),'.2f'))
    print_text += "  |"+" "*(9-len(str(test_data_set[i])))+str(test_data_set[i])+" "*6+"|"+" "*(10-len(est_sal))+est_sal+" "*4+"|\n"


print_text += "  |"+"_"*30+"|"+"\n"*3


print(print_text)