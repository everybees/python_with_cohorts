value_of_e=1

numerator=1
denominator=1

for script in range(1,11):
    value_of_e =float(numerator / denominator)
    print(f"the value of e is: {value_of_e:>.2f}")
    denominator +=1
    print(denominator)
    denominator *= denominator
    
    # value_of_e =float(numerator / denominator)
    # print(f"the value of e is: {value_of_e:>.2f}")
    # denominator -=1
    # print(denominator)
    # print(f"the value of e is: {value_of_e:>.2f}")
    # print(denominator)
  