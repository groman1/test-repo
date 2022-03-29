import re

#Capturing First Name and Appending Player Number Based on Last Name.

#Capture First Name
regex = r'((Joel|Kevin|Lebron).*)';

#Rules to Match Last Name
regex1 = r'Embiid$';
regex2 = r'Durant$';
regex3 = r'James$';

#****************************************************************************

pattern = re.compile(regex, re.IGNORECASE)

string = r'Joel Embiid'

#Test Strings:
#Joel Embiid, append 21 
#Kevin Durant, append 7 
#Lebron James, append 23
#Stephen

#****************************************************************************

firstSearch = re.finditer(pattern, string, flags = 0)

for match in firstSearch: 
    initialMatch = match.group()

    #Only Run secondSearch if Player has a Last Name

    secondSearch = re.finditer(regex1, initialMatch, flags = 0) #Need to Loop Through all Last Name Rules

    for match in secondSearch:
        secondMatch = match.group()

        #If Statement for Different Endings Here
        print(secondMatch + ' 21')


#How Can I Loop Through the Different Last Name Rules?
#Is There a Better Way to Append to a Match other than an If Statement?
#How to Run secondSearch for specific Last Name Case?




