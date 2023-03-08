while True :
  try :
    s, t = input().split()
    
    value = 0
    flag = 0
    for i in range(len(t)) :
      if t[i] == s[value] :
        value += 1
        if value == len(s) :
          flag = 1
          break

    if flag == 1 :
      print('Yes')
    else :
      print('No')

  except :
    break