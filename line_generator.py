import os
import markovify
from random import randrange

def get_line():
    lines = []
    with open(os.path.dirname(os.path.abspath(__file__)) + "/script-parser/lines.txt", "r") as lines_file:
        lines = lines_file.readlines()
    return lines[randrange(len(lines))]

def gen_line():

    # get lines file
    with open(os.path.dirname(os.path.abspath(__file__)) + "/script-parser/lines.txt", "r") as lines_file:
        text = lines_file.read()

    # create text model
    textModel = markovify.Text(text, 2)
    genSentence = None

    # generate sentence
    boolGoodSentence = False
    while not boolGoodSentence:
        genSentence = textModel.make_short_sentence(40)
        if not genSentence is None and not genSentence in text and len(genSentence) > 30 and len(genSentence) < 50:
            boolGoodSentence = True
    return genSentence