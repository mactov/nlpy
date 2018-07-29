import re


class Parser:
    """ This class contains the basic feature to parse text"""
    
    def __init__(self, text):
        self.sentence_separators = ['.', '!', '?']
        self.word_separators = [' ', ',', ':']
        self.text = text

    def list_sentences(self):
        """ This method splits the text that was passed to the parser and
        returns the list of all the sentences without the marks."""
        txt = self.text
        for sep in self.sentence_separators:
            txt = txt.replace(sep, '#')
        return [snt.strip() for snt in re.split('#', txt) if len(snt)>0]

    def list_words(self, flat=True, count=False):
        """ This method splits the text that was passed to the parser and
        returns the list of all the words. The list can be embedded (one
        sublist per sentence) or flat. Default is flat."""
        txt = self.text
        if flat:
            for sep in self.sentence_separators:
                txt = txt.replace(sep, '')
            for sep in self.word_separators:
                txt = txt.replace(sep, ' ')
            return [w.strip() for w in re.split(' ', txt) if len(w)>0]
        else:
            result = []
            lst_snt = self.list_sentences()
            for s in lst_snt:
                for sep in self.word_separators:
                    s = s.replace(sep, ' ')
                result.append([w.strip() for w in re.split(' ', s) if len(w)>0])
            return result

