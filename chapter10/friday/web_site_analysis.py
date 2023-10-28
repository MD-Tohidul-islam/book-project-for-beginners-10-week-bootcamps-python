#  import all necessary libraries
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from bs4.element import Comment
from IPython.display import clear_output
#  filter article words and hidden characters
def filter_waste(word):
    bad_word = ("the", "a", "in", "of", "to", "you", '\xa0', "and",
            "at", "on", "for", "from", "is", "that", "his",
            "are", "be", "-", "as", "&", "they", "with", "how",
            "was", "her", "him", "i", "has", "|")
    if word.lower() in bad_word:
        return False
    else:
        return True
#  scraping the web site
#  request site and return top 7 used words
#  filter out all elements that do not contain text that appears on site
def filter_tag(element):
    if element.parent.name in ['style','script','head','title','meta','[document]']:
        return False
    if isinstance(element,Comment):
        return False
    return True
def scrape(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content,'html.parser')
    text = soup.find_all(text = True)  # will get all text within the document
    # print(soup.prettify())  # remove after runs properly
    # print(text)  # remove after runs properly
    visible_text = filter(filter_tag,text)
    word_count = {}
    for text in visible_text:
    #    print(text)  # remove after runs properly
        words = text.replace("\n","").replace("\t","").split("")  # replace all hiddenn chars
        words = list(filter(filter_waste,words))
        for word in words:
            #  (word,end=' ')  # remove after runs
            if word!='':  #  if it doesn't equal an empty string
                if word in word_count:
                    word_count[word] +=1
                else:
                    word_count[word] = 1
        #print(word_count)  # remove after runs properly
        word_count = sorted(word_count.items(),key=lambda kv:kv[1],reverse=True) # sort the value
        return word_count[:7]
#  graph results of top 7 words
def display_results(words,site):
    count = [item[1] for item in words][::-1]  # reverse order
    word = [item[0] for item in words][::-1]  # get word out of reverses order

    plt.figure(figsize=(20,10))  # define how large the figure appears
    plt.bar(word,count)
    plt.title('Analyzing top words from:{}...'.format(site[:50]),
              fontname='Sans Serif',fontsize = 24)
    plt.xlabel('words',fontsize = 24)
    plt.ylabel('# of appearances',fontsize = 24)
    plt.xticks(fontname="Sans Serif", fontsize=20)
    plt.yticks(fontname="Sans Serif", fontsize=20)
    plt.show()
#  creating the main loop
# main loop should ask if user wants to scrape
while input('would you like to scrape a website (y/n)') == 'y':
    try:
        clear_output()
        site = input('Enter a website to analyze: ')
        top_words = scrape(site)
        top_word = top_words[0]  # tuple of (word,count)
        #  print(the top word is :{}'.format(top_word[0]))
        display_results(top_words,site)
        # print(site)  # remove after runs properly
    except:
        print('Something went wrong, please try again.')
print('Thanks for analyzing! Come back again!')





