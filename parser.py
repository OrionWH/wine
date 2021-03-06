#!/usr/bin/env python3

import os

class Parser():

    def read_page(self, filename):
        code_part = False
        page = ""

        if not os.path.exists(filename):
            page = "404"
            return page

        with open(filename) as f:
            line = f.readline()
            while line:
                if len(line) > 2:

                    # Heading
                    if line[0:3] == '::h':
                        l = list(line)
                        del(l[0:4])
                        del(l[-1])
                        line = ''.join(l)
                        #print("<h3>{}</h3>".format(line))
                        page += "<h3>{}</h3>".format(line)

                    # Code _on_    
                    elif line[0:3] == '::c':
                        #print("<pre><code>")
                        page += "<pre><code>"
                        code_part = True

                    elif line[0:3] == "::\n":
            
                        # Code _off_
                        if code_part == True:
                            #print("</code></pre>")
                            page += "</code></pre>"
                            code_part = False

                    else:
                        #print(line, end = '')
                        page += line
                else:
                    #print(line)
                    page += line
                line = f.readline()

        return page


