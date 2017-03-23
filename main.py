#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	self.response.write(self.buildForm())

    def post(self):
    	message = self.request.get("msg")
    	rotate_by = self.request.get("rot")
    	if rotate_by == "":
    		rotate_by = 13
    	else:
    		rotate_by = int(rotate_by)

    	encrypted = cgi.escape(caesar.encrypt(message,rotate_by))

    	self.response.write(self.buildForm(encrypted))

    def buildForm(self,text=""):
    	header = "<h2>Caesar Encryption</h2>"
    	textarea = "<textarea placeholder='Enter a Message' required='true' name='msg'>" + text + "</textarea>"
    	rotation = "<br/><label>Rotate By:<input type='number' name='rot'/></label>"
    	button = "<br/><input type='submit' value='Encrypt/Decrypt' />"
    	form = "<form method='post'>"+ textarea + rotation + button + "</form>"

        return header + form

routes = [
    ('/', MainHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
