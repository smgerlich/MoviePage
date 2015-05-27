READ ME

Requirements:

1. 	Python 2.7.9 (I think it should work with any 2.7.x version, but no guarantees).
2. 	The Google Python API client. To get the API client, use 
	
		$ sudo pip install --upgrade google-api-python-client

Instructions to run:

1. 	Clone the repository from github or download the zip and extract.
2. 	Open MoviePage.py to edit it and insert a Youtube API key in line 4. I've included my API key in 
	the email submitting this project to Udacity. To anyone other than Udacity, git yer own dang key.
3.	On Mac and Linux, give executable permissions to server.py, MoviePage.py and media.py:

		$ chmod +x server.py
		$ chmod +x MoviePage.py
		$ chmod +x media.py
		$ chmod +x media.pyc
	
4.  Run server.py to start a light http server with basic CGI scripting. 
5. 	Open a Chrome window to http://localhost:8000/MoviePage.py. The CSS is a little off in IE and FF, 
	and it is really slow in IE.

I used this project as an opportunity to learn a little bit about Google's Polymer framework, but
because I am using a python script to grab the data and insert it into templates, it was a bit unwieldy. 
I learned that you probably don't want to use Polymer unless you're really going to use it the way Google 
intends -- with actual two-way binding, their XHR implementation, and their declarative event handling. 

Thanks to Jack Trades at Pointless Programming and his blog entry 
at	https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/ for
the cgi scripting file. 

Also, in case it's not obvious, this was a programming project for a course. There're a lot of ways
in which it is not production-ready, and you probably shouldn't use it for much of anything (not that
you'd really want to). However, if you do want to, please feel free (as in speech and beer) to use it
under the terms of the BSD license:




// Copyright 2015 Sean Gerlich. All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:
//
//    * Redistributions of source code must retain the above copyright
// notice, this list of conditions and the following disclaimer.
//    * Redistributions in binary form must reproduce the above
// copyright notice, this list of conditions and the following disclaimer
// in the documentation and/or other materials provided with the
// distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   

Where individual files are subject to copyrights by third parties, this is indicated in the file itself.