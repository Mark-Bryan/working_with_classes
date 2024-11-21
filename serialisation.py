# Converting code to text and the text back to code again

import json

user = {
    "firstName" : "Albert",
    "lastName" : "Smith",
    "dateOfBirth" : "12/11/2024",
    "address" : "Cameroon"
}

newFile = open("userFile.txt", 'w')
newFile.write(json.dumps(user))
newFile.close()
