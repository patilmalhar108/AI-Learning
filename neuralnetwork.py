score = 0
def q1():
  q1 = "What do we call the first layer of this neural network?"
  a1 = input("Enter your answer : ")
  a1 = a1.lower()
  if a1=='input layer':
    s = 1
  else:
    s=0
  return s

def q2():
  q2 = "How many number of neurons can be there in the first layer of this neural network?"
  a2 = int(input("Enter your answer : "))
  if a2==8:
    s = 1
  else:
    s=0
  return s

def q3():
  q3 = "How many hidden layers are present in this neural network?"
  a3 = int(input("Enter your answer : "))
  if a3==3:
    s = 1
  else:
    s=0
  return s

def q4():
  q4 = "There can be any number of neurons in the hidden layer of this neural network. True or False?"
  a4 = input("Enter your answer : ")
  a4 = a4.lower()
  if a4=='true':
    s = 1
  else:
    s=0
  return s

def q5():
  q5 = "What do we call the last layer of this neural network?"
  a5 = input("Enter your answer : ")
  a5 = a5.lower()
  if a5=='output layer':
    s = 1
  else:
    s=0
  return s

def q6():
  q6 = "How many number of neurons can be there in the last layer of this neural network?"
  a6 = int(input("Enter your answer : "))
  if a6==1:
    s = 1
  else:
    s=0
  return s

score += q1()
score += q2()
score += q3()
score += q4()
score += q5()
score += q6()
print("Your score is :", score)