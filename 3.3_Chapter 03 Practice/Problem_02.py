# This program changes the given template according to the specific requirements 
# letter = """Dear|<Name>|  You are selected!  Date|<00-00-0000>|"""
letter = """Dear |<Name>|  \nYou are selected!  \nDate |<00-00-0000>|"""
print(letter.replace("|<Name>|", "Zeeshan"). replace("|<00-00-0000>|", "12-12-2025"))
# In the replace function two replace terminologies are being used actually this is called chaining.