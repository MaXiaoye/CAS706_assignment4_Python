# CAS706_assignment4_Python

Assignment 4
Scripting/Programming with libraries
This assignment is all about finding the right libraries as well as the right level of expressiveness to code what seems like a very complex task in very few lines of (still readable!) code.

First, you should write a program which takes a command-line parameter for a "search", then makes a query (DuckDuckGo, Bing, etc, all have APIs) to get (the names of) files containing HTML -- you might even want to make your query more precise and get certain flavour(s) of HTML. You are to take 500 files from the web (obtained from your query), and run these files/sites through the W3C HTML Validator. You can use the validator locally, but you get extra points if you can use the online version of the Validator hosted on the W3C site. [In other words, you don't even need to download the files.] Grab all the errors and warnings you get, and collect some statistics about this "bad html", and output these statistics. Your code should be no longer than 100 lines of well-formatted code. Fewer lines is better, as long as the code remains readable.

Beware: many search API only allows some number of free searches per day, so do not debug your code by massive testing, as you will get billed for it! Also, don't blast too much to the W3C site all at once as you'll get blacklisted. So it is a good idea to have a list of files available without doing the query, and the validator available locally, to do testing. Bonus marks for being able to do this in the same code with a command-line switch.
----------------------------------

Usage:
Just run search.py

Output is written in a file. Location: /src/data/nnit.txt 
Content in output is lines in format: link errors: n warnings: n
Such as: http://www.baidu.com/link?url=5fyemz2oQ0Veb7SZAf2g4sco8OHHKtMLEQ8MwrzIZLXDSnJMj0N9O1BLXszPxS3ZJPRgPixMovPBP622stVqeK errors: 31, warnings: 11

Input keyword for searching after seeing hint on command line: 

Start:
Please input keyword for searching: nnit
End！  --> When “end” appears that means validation is done.

In code, I just send one page result to validator to prevent from black list that mymap=['0'].
If we want 500 files, then we need 50 pages so just modify mymap to mymap=['0','1', ... '50',]
I didn’t test 50 pages because seems 500 requests will get blacklisted by w3c validator.  I tested 2 pages that it works well. So I consider it will also work well for 50 pages :)
