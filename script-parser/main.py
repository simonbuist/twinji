import requests
import os

def main():
    print("Running")
    print(os.path.dirname(os.path.abspath(__file__)) + "/script.txt")
    script_text = ""

    # open the script file
    with open(os.path.dirname(os.path.abspath(__file__)) + "/script.txt", "r") as script_file:
        script_lines = script_file.readlines()
        script_text = "~twinji~".join(script_lines)
        script_text = script_text.replace("Shinji :", "Shinji:")



    print(script_text)

    lim = 200

    with open(os.path.dirname(os.path.abspath(__file__)) + "/lines.txt", "w") as lines_file:

        

        
        while script_text != "":
            index = script_text.find("Shinji:")

            # check if we've gotten all the Shinji lines
            if index == -1:
                break

            
            script_text = script_text[index:]
            # index = script_text.find("~twinji~\n~twinji~")

            # index2 = script_text[script_text.find(":")+1:].find(":")

            index = round(1/max(1/script_text.find("~twinji~\n~twinji~"), 1/script_text[script_text.find(":")+1:].find(":")))

            line = script_text[:index]
            line2 = script_text[:index + 50]
            print(line)

            # remove \n's, indents, and "Shinji:"
            line = " ".join(line.split()) + "\n"
            line = line.replace("~twinji~", "")
            line = line.replace("Shinji:", "").lstrip()
            line = line.replace("-", "")
            line = line.replace("  ", " ")


            script_text = script_text[index:]
            if len(line) > 10:
                lines_file.write(line)

            #lim -= 1
            if lim == 0:
                break

    print("done")


main()