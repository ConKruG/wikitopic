# Overview of the package wikitopic

Wikitopic is an explicit topic extractor from English documents. It is developed in Emerging Risk Group at Kemmy Business School, University of Limerick as a part of another research in Cyber Risk Prediction by Dr Arash Kia and Dr Finbarr Murphy. 

The package uses the acsending sorted frequent words in a list of lists structure where each list stores all the words with the same frequency. The words are extracted from the pre-processed document. Each bunch of words with same frequency are added to a search string one by one to find the best matching topic from Wikipedia. Wikitopic addes words to its search expression list by list from the frequent words sorted list of lists and searches Wikipedia with it until it reaches the minimum search result (The last search result before empty search result). The first item in the the minimum search list result will be the best matched topic of the document. Wikitopic also outputs a list with the first item of the search list for all the steps until reaching the final result. This list shows a top-down path from a general topic to the most specific topic for the document. Wikitopic also produces a list of top n frequent words as the third element of its output.

### Citation information
Please if you use the package in your research, cite it in your paper like this:
Kia, A. N., Murphy, F., 2020. Wikipedia topic extractor. GitHub; [accessed *date*]. https://github.com/conkrug/wikitopic. 
## Installation information and requirements
pre-requisites for the package are nltk and wikipedia package in python. Also re, string, and collections must be installed first.
If nltk and wikipedia packages are not installed you can install them with these commands:

```sh
pip install nltk
pip install wikipedia
```

For Anaconda distribution you can do the following:

```sh
conda install -c conda-forge wikipedia
conda install -c anaconda nltk
```

After installing the pre-requisites (if not installed before!), you can install the wikitopic package with this command:

```sh
pip install wikitopic
```

## Quick-start examples
This lines of code show a simple example of topic extraction with wikitopic:

```sh
from wikitopic import wikitopic
print(wikitopic.WikiTopicExtractor("This is a sample English text"))
```

As you can see, it is possible to put a sentence directly as input of the WikiTopicExtractor class and get the output.

>Output:
>Best topic extracted for the document is: Lorem ipsum
>Path to the topic is:
>['No Topic', 'Lorem ipsum']
>5 most frequent words in the document are: 
>['text', 'english', 'sample']

Or you can read a text file from a path and find the wikitopic:

```sh
from wikitopic import wikitopic as wik

path = 'c://cav//taxonomy//sampleText.txt' #Change the path according to your own system
text = wik.read_from_file(path)
w = wik.WikiTopicExtractor(text, 10) #10 for top 10 frequent words
result = w.output_topic()

print("Best matched topic is: ", result[0])
print("From general to specific topic: ", result[1])
print("Top 10 frequent words", result[2])
```
### Acknowledgements
This work was part of a bigger project that was funded by the European Union’s Horizon 2020 research and innovation program via MALAGA Project under grant agreement No 844864 funded this work.
