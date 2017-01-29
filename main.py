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
import caesar # three previous functions being recycled
import cgi # so we dont have to deal with < > stuff messing things up

header = "<h1> Ara's Web Caesar App </h1>"

# this is what I want to show on the get and post pages, keeping the code dry
def build_page(textarea_content):
    rot_label = "<label>Rotate by how many numbers? </label>"
    rotation_input = "<input type='number' name='rotation_number'/>"

    message_label = "<label>Please type any message: </label>"
    textarea = "<textarea name='message_textarea' style='height: 50px; width: 200px;'>" + textarea_content + "</textarea>"

    submit_label = "<label>Now click submit and watch the action! "
    submit = "<input type='submit' name='mess'/>"

    form = ("<form method='post' action='/'>" +
            rot_label + rotation_input + "<br><br>" +
            message_label + textarea + "<br><br>" +
            submit_label + submit +
            "</form>")

    return header + form


class MainHandler(webapp2.RequestHandler):

    # the initial place we go
    def get(self):
        content = build_page("(type anything in here)")
        self.response.write(content)

    # where we go to see the message via the form method
    def post(self):
        message = self.request.get("message_textarea")
        num = int(self.request.get("rotation_number"))
        encrypted_message = caesar.encrypt(message, num)
        escaped_message = cgi.escape(encrypted_message)

        content = build_page(escaped_message)
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler) # the only route I'm using for this app
], debug=True)
