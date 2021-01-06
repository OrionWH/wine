#!/usr/bin/env python3

class Parser():

    def read_page(self, filename):
        code_part = False

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
                        print("<h3>{}</h3>".format(line))

                    # Code _on_    
                    elif line[0:3] == '::c':
                        print("<pre><code>")
                        code_part = True

                    elif line[0:3] == "::\n":
            
                        # Code _off_
                        if code_part == True:
                            print("</code></pre>")
                            code_part = False

                    else:
                        print(line, end = '')
                else:
                    print(line)
                line = f.readline()

p = Parser()

p.read_page("random.tt")

