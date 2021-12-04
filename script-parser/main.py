from os import path

def getFolder(file):
    return path.join(path.dirname(path.abspath(__file__)), file)

def main():
    print("Running")
    print(getFolder("script.txt"))
    script_text = ""

    # open the script file
    with open(getFolder("script.txt"), "r", encoding='utf-8') as script_file:
        script_lines = script_file.readlines()
        script_text = "~twinji~".join(script_lines)
        script_text = script_text.replace("Shinji :", "Shinji:")

    with open(getFolder("lines.txt"), "w", encoding='utf-8') as lines_file:

        while script_text != "":
            index = script_text.find("Shinji:")

            # check if we've gotten all the Shinji lines
            if index == -1:
                break

            script_text = script_text[index:]

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

    print("done")


main()