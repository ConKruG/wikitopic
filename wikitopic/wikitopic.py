# Emerging Risk Group 
#
# A tool to extract topics of any English document from wikipedia!
#
# Part of MALAGA research by: Dr. Arash N. Kia, and Dr. Finbarr Murphy
# Code and Algorithm: Arash Kia
#
# This is a part of work that was funded by the European Union’s Horizon 2020 research and 
# innovation program via MALAGA Project under grant agreement No 844864 funded this work
#
###########################################################

from nltk import pos_tag
from nltk import word_tokenize
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords

from re import sub
from re import escape
from re import compile as comp

from string import punctuation
from string import printable

from collections import Counter

from wikipedia import search


class WikiTopicExtractor:
    
    #Default number of most frequent words that will be returned and default input text as empty
    n = 5
    text = ''
    
    def __init__(self, text = '', n = 5):
        self.n = n
        self.text = text
    
        
    ###LEMATIZER
    ############   
    
    def get_wordnet_pos(self, treebank_tag):
    
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN
        
    def normalize_text(self, text):
    
        lmtzr = WordNetLemmatizer().lemmatize
        
        word_pos = pos_tag(word_tokenize(text))
        lemm_words = [lmtzr(sw[0], self.get_wordnet_pos(sw[1])) for sw in word_pos]

        return [x.lower() for x in lemm_words]

    
    def prepare_text(self):
    """ INPUT: A STRING
    ### OUTPUT: A LEMATIZED STRING WITHOUT NUMBERS, PUNCTUATIONS, AND STOP WORDS
    """
        descriptions = []
        descriptions.append(self.text)
        corpus = [self.normalize_text(s) for s in descriptions]
        descriptions = [' '.join(s) for s in corpus]

        new_desc = []
        for t in descriptions:
            new_desc.append(' '.join([word for word in t.split() if word not in stopwords.words("english")]))

        new_desc2 = [sub(r'\b[0-9]+\b\s*', '', s) for s in new_desc]

        final = new_desc2[0]

        #final = "".join(l for l in final if l not in string.punctuation)

        regex = comp('[%s]' % escape(punctuation))
        final = regex.sub(' ', final)

        p = set(printable)
        final = ''.join(filter(lambda x: x in p, final))
        final = ' '.join( [w for w in final.split() if len(w)>1] )

        return final
    

    def word_count(self, T):
        
        """ Parameters: T (str): Prepared lemmatized English text without stop-word
            Returns: List of lists of frequent words, n top frequent words"""
        
        counts = Counter()
        counts.update(word.strip('.,?!"\'').lower() for word in T.split())
        sorted_count = {k: v for k, v in reversed(sorted(counts.items(), key = lambda item: item[1]))}

        top_words = list(sorted_count.keys())
        if len(top_words) >= self.n:
            top_n = top_words[:self.n]
        else:
            top_n = top_words

        y = list(sorted_count.items())
        v1 = 0
        l = []
        L = []
        c = 0
        for i in y:
            v2 = i[1]
            if v1 == v2:
                l.append(i[0])
                c = c + 1
            else:
                if l != []:
                    L.append(l)
                l = []
                l.append(i[0])
                c = c + 1

            v1 = v2

        L.append(l)

        return L, top_n
    
    
    def doc2top(self, wordcount_list):
        
        """ Parameters: wordcoult_list: list of lists
            Returns: str, list: extracted topic from Wikipedia, a list of topics extracted until finding the 
            best topic"""
        
        query = []
        old_result = 'No Topic'
        result_history = []
        result_history.append(old_result)
        #print('INPUT:')
        #print(wordcount_list)

        for q in wordcount_list:
            #print('Q: ', q)
            query = query + q
            final_query = " ".join(query)
            #print(len(final_query))
            if len(final_query) == 0:
                return 'Input text does not have enough information', result_history
            if len(final_query) < 300:
                result = search(final_query)
                if len(result) > 0:
                    if result_history[-1] != result[0]:
                        result_history.append(result[0])
            else:
                return old_result[0], result_history
            #print('RESULT: ', result)
            if len(result) == 1:
                #print('First IF')
                return result[0], result_history
            if len(result) == 0:
                #print('Second IF')
                return old_result[0], result_history

            old_result = result

        return old_result[0], result_history
    
    def output_topic(self):
        
        """Returns: str, list, list: best topic, list of topics until reaching the best topic, 
        top n frequent words in the input text"""
        
        T = self.prepare_text()
        L, top_n = self.word_count(T)
        best_topic, path_to_topic = self.doc2top(L)
        
        return best_topic, path_to_topic, top_n
    
    def __str__(self):
        
        T = self.prepare_text()
        L, top_n = self.word_count(T)
        best_topic, path_to_topic = self.doc2top(L)
        return "Best topic extracted for the document is: " + str(best_topic) + "\n" + "Path to the topic is:\n" + str(path_to_topic) + "\n" + str(self.n) + " most frequent words in the document are: \n" + str(top_n)



### INPUT LOADING FROM A FILE
def read_from_file(path):

    """To read from a text file with utf8 encoding
        Parameters: path of the file
        Returns: str: content of the text file"""
    
    with open(path, 'r', encoding = "utf8") as file:
        text = file.read().replace('\n', '')

    return text

if __name__ == "__main__":
    
    path = 'c://cav//taxonomy//sampleText.txt' #Change the path according to your own system
    text = read_from_file(path)
    
    #w = WikiTopicExtractor("This is a sample English text")
    #result = w.output_topic() #result[0]: topic, result[1]: path to topic, result[2] = frequent words
    
    print(WikiTopicExtractor(text, 10))
