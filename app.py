# INPUTS NEEDED FOR POWER QUERY EDITOR CODE CHANGES
sheet = input("Sheet name: ")
client = input("Client: ")
name = input("Engagement Name: ")
code = input("Engagement Code: ")
partner = input("Engagement Partner: ")


string = '''*PUT YOUR BASE POWER QUERY EDITOR CODE HERE BETWEEN TRIPLE SINGLE QUOTES TO KEEP FORMAT*'''

string = string.replace("clnt", client).replace("eng nm", name).replace("eng cd", code).replace("eng prtn", partner).replace("sht", sheet)

# RESULTING POWER QUERY EDITOR CODE
print(string)
