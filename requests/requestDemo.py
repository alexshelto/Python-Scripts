#Alex Shelton requests demo

import requests

URL = 'https://github.com/alexshelto'
r = requests.get(URL)
#print(r) #prints 200 response

#Pulling Content from page.

#print(dir(r)) #Prints the available objects and methods
#print(help(r)) #Prints more detailed list
#print(r.text) #Prints content of text in unicode <html code> 

#Downloading an image: 
#r1 = requests.get("Image download link ")
#print(r.content) #prints image bytes

#saving:
# with open('comic.png', 'wb') as f: #wb = write bytes
#     f.write(r1.content)

# print(r.status_code) #200 = sucsess,300s = redirects, 400 = client errors, 500 = server error
# print(r.ok) #returns true for anything < 400 response



## Advanced features


# payload = {'page': 3, 'count': 25}
# URL = 'https://httpbin.org/get'

# r = requests.get(URL, params=payload)
# print(r.url)



#Posting

# payload = {'username': 'bobby', 'password': 'Testing123'}
# URL = 'https://httpbin.org/post'

# r = requests.post(URL, data=payload)
# print(r.json())

