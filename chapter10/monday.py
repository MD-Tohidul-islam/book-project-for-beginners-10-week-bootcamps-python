# Virtual Environments and requests Module
# sending a request and logging the response code
import requests
r = requests.get('https://api.github.com/users/Connor-SM')
print(r)
print(type(r))
# accessing the content that we reqested from the URL
data = r.content
print(data)
# # converting the response
data = r.json()  # converting the data from a string to a dictionary
for k, v in data.items():
    print('key:{}\t value:{}'.format(k,v))
print(data['name'])  # accessing data directly
#  passing parameters
#  outputting specific key-value pairs from data
r = requests.get("https://api.github.com/search/repositories?q=language:"
                 "python")
data = r.json()
print(data['total_count']) # output the total number of repositories that use python


