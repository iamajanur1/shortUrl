
# correctName = "sintu"
# name = input("enter the secret name: ")
#  (name == correctName) ?
#     print(f"{name}'s name is AJANUR RAHMAN is a good boy, he will be happy to see you again.")  
# :
#     print ("you are not {0}, please try again".format (correctName))

correctName = "sintu"
name = input("Enter the secret name: ")
print(f"{name}'s name is AJANUR RAHMAN, he is a good boy and will be happy to see you again." if name == correctName else f"You are not {correctName}, please try again.")
