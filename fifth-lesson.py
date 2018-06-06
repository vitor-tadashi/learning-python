from urllib.request import urlopen

def read_text():
    textFile = open(r"/home/tadashera/Documents/requests/movie_quotes.txt")
    content = textFile.read()
    textFile.close()
    check_profanity(content.replace('\n', ' ').replace('\r', ''))


def help_object(object):
    help(object)


def check_profanity(text):
    print(text)
    connection = urlopen("http://www.wdylike.appspot.com/?q=" + text, None, None)
    output = connection.read()
    print(output)

    if output == b'true':
        print("PROFANITY ALERT!!")
    elif output == b'false':
        print("This document has no curse words!")

    connection.close()


read_text()