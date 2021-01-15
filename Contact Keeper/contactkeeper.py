# Name : KUSHAGRA PATHAK
# ID : 201801005

from sortedcontainers import SortedDict
import sys
import pandas as pd

# Initialising our phonebook
phonebook = SortedDict()

pb = pd.DataFrame(columns=['Name','Contact Number(s)']) 


while 1 :

  choice = input('=========CHOOSE AN OPERATION=========\nEnter the operation you want to perform : \n 1. Add \n 2. Query \n 3. Delete \n 4. Exit \n ======================================\n')
  choice = choice.title()

  if choice == '2' or choice == 'Query' :

    print('\n ============= QUERY ============== \n')

    print('Your Phonebook : \n',pb.head())

    # Input keyword from user
    keyword = str(input('Input the keyword you want to search : '))

    All_Con = phonebook.keys() 
    All_Con = list(All_Con)

    res = []
    for i in All_Con : 
      if i.find(keyword)!=-1:
        res.append(i)

    if len(res)==0:
      print('No contacts matching this key exists! :/','\n')
    else : 
      print(f'All keys matching the keyword "{keyword}"\n', res)

      for i in res: 
        print(i)

      while 1 :
        input_name = str(input('Type a contact name to retrieve its information : ' ))
        input_name = input_name.title()

        if phonebook[input_name] == 0: 
          print('Please enter the exact name shown in the above list!')
        else :
          print(input_name,':', phonebook[input_name])
          break

      print('Thank you for querying our databases. Have a good day!')

  if choice == '1' or choice == 'Add' :
    
    print('\n ============= ADD ============== \n')
    Name = str(input('Input name of the contact : '))
    Name = Name.title()
    Contact = str(input('Enter a valid number : '))
    
    while len(Contact) != 10 :
      Contact = str(input('Enter a valid 10 digit number : ')) 

    found = 0

    try : 
      phonebook[Name].append(Contact)
      found = 1
      print(f'A contact with name {Name} already exists! the contact number will be appended...')
    except :
      found = 0 
    
    if found==0 :

      Contact = [Contact]
      a_contact = {
          Name : Contact
      }
      phonebook.update(a_contact)

      print(f'Contact with details : \n Name : {Name} \n Phone : {Contact} \n has been successfully added!')

    tp = pd.DataFrame(columns=['Name','Contact Number(s)'])
    
    print('\n Updated Phonebook : \n')

    pcnt=0
    for i in phonebook : 
      nr = pd.Series(data = {'Name' : i,'Contact Number(s)' : phonebook[i]} , name = str(pcnt + 1))
      pcnt+= 1
      tp = tp.append(nr)

    pb = pb.iloc[0:0]
    pb = tp
    print(pb.head(10),'\n')

  if choice == '3' or choice == 'Delete' :
    
    print('\n =============== DELETE ============== \n')
    
    for i in phonebook :
      print(i , phonebook[i] ,'\n')
    
    name = str(input('Choose which contact to delete by typing in name :'))
    name = name.title()

    try : 
      del phonebook[name]
    except :
      print('No such contact listed! \n')

    print('\n Updated Phonebook : \n')
    
    tp = pd.DataFrame(columns=['Name','Contact Number(s)'])

    pcnt=0
    for i in phonebook : 
      nr = pd.Series(data = {'Name' : i,'Contact Number(s)' : phonebook[i]} , name = str(pcnt + 1))
      pcnt+= 1
      tp = tp.append(nr)

    pb = pb.iloc[0:0]
    pb = tp
    print(pb.head(10),'\n')


  if choice == '4' or choice == 'Exit' :
    print('\n =============== EXIT ============== \n')
    print('Thank you for using our phonebook services. Have a good day!')
    sys.exit("User chose to exit the program")

