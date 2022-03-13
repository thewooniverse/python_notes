import requests

r = requests.get('https://xkcd.com/353/')
print(r)
## prints <Repsonse [200]> object

# print(dir(r))
# print(dir(requests))
## you can dir(module) or even dir(object), so when you print a dir(object), it lists out all the methods
## attributes etc... that the object has, in this case, the r, response object.
## for more detail, you can do a print(help(object or module))
# print(help(r))
## This really shows me how to use new modules and libraries, and learn about objects;
### I feel way less intimidated by learning new mods.

## So from help(r) I know that response.text - which is "content of response in unicode".
# print(r.text)
## This prints out the HTML, and this is the HTML for the page that we just looked at.
## To parse this information, we should use a HTML parser to do that.
## This is how we get the source HTML code of the website given to the get function.


## Though if you wanted to download the image,
ri = requests.get('https://imgs.xkcd.com/comics/python.png')
# print(ri.content)
## response_object.content prints out the bytes for the image.

# with open('comic.png', 'wb') as f:
#     f.write(ri.content)
## this creates a new file, by opening it in 'write bytes' mode as f, and f.write(ri.content)
## you can see it has done this in the current working directory.
### This gives me a project idea, how about if I jumbled up these byte codes... to create a mosaic thing that
### jumbles up images.

# print(r.status_code)
## this prints out the status code, in our case it was 200, which I know means is a good response.
## You can use these response.status_codes, to track websites and their status.
## 200s are success, 300s are redirects and 400s are client errors, 500s are the server errors.

# print(r.ok)
## this simply prints out True, for anything that is less than a 400 response;
## Any kind of server or client side error will return False.

# print(r.headers)
## This prints out all the headers that come back with the response;
## Like server is nginx, content type is text/html (this is image/png for the ri file)
## httpbin.org helps us test all the different queries.


payload = {'page': 2, 'count': 25}
rhttpg = requests.get('https://httpbin.org/get', params=payload)
## you can a lot of the times do things like ?page=2&count=1 << but this is prone to errors
## so the HTML library allows us to pass a dictionary and converts it to the appropriate URL for us.
## this is what we're doing in the payload variable, which is a dictionary of the different
## arguments I want to pass into the get request / query.
## I then pass this into the get request as the params argument
## this approach is less error prone & readable because you are using a clean dictionary instead of hard coding the URL

# print(rhttpg.text)
## you can see that the response object rhttps -- had args, page = 2, count = 25
## you can see the changed url with the params by printing...
# print(rhttpg.url)


## POST ##
## you would do something like this when you might want to post something like a form data to a route or sth.
# payload2 = {'username': 'Woo', 'userid': '0001', 'password': 'testing'}
# rhttpp = requests.post('https://httpbin.org/post', data=payload2)
## pay attention to the requests.post, and data argument.
# print(rhttpp.text)
## in this print, args: is empty, but your payload2 is populated into the "form": key in the response object.
## sometimes you need to look into the HTML source code to find out what exactly you need to fill out in the form.
## / what the website expects.


## we are getting a json response back from the http website;
## It is very common to receive JSON response when working with APIs
## and knowing this, you can also the .json() method
# print(rhttpp.json())
# r_dict = rhttpp.json()
## this created a python dictionary out of the json response.
## you can save it into a variable, and access it like any other dictionary.
## as I already know, almost every language has built in functions to both create and parse JSON objects
## like the json module for python, but the response object's .json() method is a nice shortcut.
# print(r_dict.get('form'))

## you can do put queries / requests with requests.put
## and for the times that login authentication is not form based, and uses basic_authentication
## then you can do that with the requests library as well.


http_auth = requests.get('https://httpbin.org/basic-auth/wooyoung/testing', auth=('wooyoungz', 'testing'))
print(http_auth.text)
## so when you get it correctly, you get returned.
# {
#   "authenticated": true,
#   "user": "wooyoung"
# }


print(http_auth)
## again, this when correct prints http response[200]
## but if you get it wrong, http_auth.text is empty, and http_auth will be a response object with status code of 401;
## 401 is an unauthorized response code.

## TIMEOUT ##
## timeouts are useful because if you don't get a response sometimes, your script can wait around forever.
## with the timeout parameter


r_delayed = requests.get('https://httpbin.org/delay/6', timeout=3)

print(r_delayed)
## if delay is less than timeout, you get the response status of 200.
## but if it is longer than the timeout, you get a request timeout




#### SUMMARY #### << this is good
## This is about 90% of what you'll use request for
## and that is really all you'll need to learn most the time for most libraries.
## so you don't need to really know all the inner workings, again, modules, APIs and INTERFACES! yay.
## so many good tools already out there.