from os import path
import markovify
import language_tool_python
from random import randrange

def getFolder(file):
    return path.join(path.dirname(path.abspath(__file__)), file)

def get_line():
    lines = []
    with open(getFolder(path.join("script-parser", "lines.txt")), "r", encoding='utf-8') as lines_file:
        lines = lines_file.readlines()
    return lines[randrange(len(lines))]

def gen_line():

    # get grammar checker
    # gram_tool = language_tool_python.LanguageTool("en-US")

    # get lines file
    with open(getFolder(path.join("script-parser", "lines.txt")), "r", encoding='utf-8') as lines_file:
        text = lines_file.read()

    # create text model
    textModel = markovify.Text(text, 2)
    genSentence = None

    # generate sentence
    boolGoodSentence = False
    while not boolGoodSentence:
        genSentence = textModel.make_short_sentence(40)
        # genSentence = gram_tool.correct(genSentence)
        if not genSentence is None and not genSentence in text and len(genSentence) > 30 and len(genSentence) < 50:
            boolGoodSentence = True
    return genSentence