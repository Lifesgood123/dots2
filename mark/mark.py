from sys import argv
import markovify

script, source = argv

def gen_print(arg1):


    with open(arg1) as f:
        text = f.read()

        #build markovian model
        text_model = markovify.Text(text)

        # Print five randomly-generated sentences
        #for i in range(5):
        #    print(text_model.make_sentence())

        # Print three randomly-generated sentences of no more than 140 characters
        for i in range(1):
            print(text_model.make_short_sentence(140))
gen_print(source)
