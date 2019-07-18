import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
import string
from collections import Counter
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
stop = set(stopwords.words("english"))
plt.style.use('dark_background')

os.chdir("C:/Users/paulb/Documents/nlp")
reviews = pd.read_csv("1429_1.csv")

#MANIPULATING DATAFRAME
##Creating valuable features
reviews.columns.values
reviews = reviews[['id', 'reviews.numHelpful', 'reviews.rating', 'reviews.text',
            'reviews.title']]

print(reviews.isnull().sum())
reviews["reviews.numHelpful"][reviews["reviews.numHelpful"].isnull()] = 0
reviews = reviews.dropna()

##Fixing text for EDA
def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

round1 = lambda x: clean_text_round1(x)

reviews["reviews.clean"] = pd.DataFrame(reviews["reviews.text"].apply(round1))
reviews["reviews.clean"] = reviews["reviews.clean"].str.split(' ').apply(lambda x: ' '.join(k for k in x if k not in stop))

##Manufacture features from text
reviews["num_chars"] = reviews["reviews.clean"].apply(lambda x: len(str(x)))
reviews["num_punctuations"] = reviews['reviews.text'].apply(lambda x: 
            len([c for c in str(x) if c in string.punctuation]) )
reviews["words_upper"] = reviews["reviews.text"].apply(lambda x: 
            len([w for w in str(x).split() if w.isupper()]))

reviews["num_chars_title"] = reviews["reviews.title"].apply(lambda x: len(str(x)))
reviews["num_punct_title"] = reviews['reviews.title'].apply(lambda x: 
            len([c for c in str(x) if c in string.punctuation]) )
reviews["words_upper_title"] = reviews["reviews.title"].apply(lambda x: 
            len([w for w in str(x).split() if w.isupper()]))

#INITIAL ASSESSMENT OF REVIEWS
##Helpfulness split
helpful_revs = reviews["reviews.numHelpful"] > 0
reviews["reviews.Helpful"] = helpful_revs

##Ratings vs Helpfulness
rating_help = pd.crosstab(index = reviews["reviews.rating"], 
                          columns = reviews["reviews.Helpful"]) 
rating_help1 = pd.crosstab(index = reviews["reviews.rating"], 
                          columns = reviews["reviews.Helpful"],
                          normalize="index") 

sns.countplot(x = 'reviews.Helpful', data = reviews)

sns.heatmap(rating_help, cmap="Reds", annot=True, cbar=False, fmt='g')
sns.heatmap(rating_help1, cmap="RdBu_r", annot=True, cbar=False, fmt='g')

#BREAKING DOWN SEGMENTS (PLOTTING FOR TEXT DIFFERENCES)
##Characters for helpful reviews
sns.distplot(reviews[helpful_revs][["num_chars"]], hist = False, rug = True)
sns.distplot(reviews[~helpful_revs][["num_chars"]], hist = False, rug = True)

##Punctuation for helpful reviews
sns.distplot(reviews[helpful_revs][["num_punctuations"]], hist = False, rug = True)
sns.distplot(reviews[~helpful_revs][["num_punctuations"]], hist = False, rug = True)

##Uppercase for helpful reviews
sns.distplot(reviews[helpful_revs][["words_upper"]], hist = False, rug = True)
sns.distplot(reviews[~helpful_revs][["words_upper"]], hist = False, rug = True)

##Characters for helpful reviews
sns.distplot(reviews[helpful_revs][["num_chars_title"]], hist = False, rug = True)
sns.distplot(reviews[~helpful_revs][["num_chars_title"]], hist = False, rug = True)

##Punctuation for helpful reviews
sns.distplot(reviews[helpful_revs][["num_punct_title"]], hist = False, rug = True)
sns.distplot(reviews[~helpful_revs][["num_punct_title"]], hist = False, rug = True)

##Uppercase for helpful reviews
sns.distplot(reviews[helpful_revs][["words_upper_title"]], hist = False, rug = True)
sns.distplot(reviews[~helpful_revs][["words_upper_title"]], hist = False, rug = True)

#SUBJECTIVITY/POLARITY ASSESSMENT
#SENTIMENT ASSESSMENT OF TEXT
pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity

reviews['polarity'] = reviews["reviews.text"].apply(pol)
reviews['subjectivity'] = reviews["reviews.text"].apply(sub)

##Positive vs negative
pos = reviews["reviews.rating"] >= 3
reviews["Sentiment"] = pos

##Helpfulness distplotting
sns.distplot(reviews[~helpful_revs][["subjectivity"]], color = "powderblue")
sns.distplot(reviews[helpful_revs][["subjectivity"]], color = "gold")
plt.legend(labels = ['Unhelpful', 'Helpful'])
plt.show()

sns.distplot(reviews[~helpful_revs][["polarity"]], color = "powderblue")
sns.distplot(reviews[helpful_revs][["polarity"]], color = "gold")
plt.legend(labels = ['Unhelpful', 'Helpful'])
plt.show()

##Plotting subjectivity and polarity
sns.scatterplot(x = "subjectivity", y = "polarity",
                linewidth = 0, alpha = 0.7, data = reviews[helpful_revs])
plt.title("Helpful Reviews: Polarity vs Subjectivity")
plt.show()

sns.scatterplot(x = "subjectivity", y = "polarity",
                linewidth = 0, alpha = 0.7, data = reviews[pos])
plt.title("Positive Reviews: Polarity vs Subjectivity")
plt.show()

sns.scatterplot(x = "subjectivity", y = "polarity", color = "y",
                linewidth = 0, alpha = 0.7, data = reviews[~pos])
plt.title("Negative Reviews: Polarity vs Subjectivity")
plt.show()

##Plotting Sentiment over Character length
fig = sns.lmplot(x = "num_chars", y = "subjectivity", hue = "reviews.rating", 
              data = reviews, col = "reviews.Helpful")
fig.set(xscale = "log", xlabel = 'Number of Char.', ylabel = 'Subjectivity', 
        ylim = (0,1))
fig.fig.suptitle('Subjectivity vs Characters', fontsize = 14)
plt.subplots_adjust(top=0.9)
plt.show()

fig = sns.lmplot(x = "num_chars", y = "polarity", hue = "reviews.rating", 
              data = reviews, col = "reviews.Helpful")
fig.set(xscale = "log", xlabel = 'Number of Char.', ylabel = 'Polarity', 
        ylim = (-1,1))
fig.fig.suptitle('Polarity vs Characters', fontsize = 14)
plt.subplots_adjust(top=0.9)
plt.show()

#WORDCLOUD AND TERM COMPARISON
##ADDING STOPWORDS
##Helpful vs Unhelpful
x = Counter(" ".join(reviews[helpful_revs]["reviews.clean"]).split()).most_common(100)
y = Counter(" ".join(reviews[~helpful_revs]["reviews.clean"]).split()).most_common(100)

x = [z[0] for z in x]
y = [z[0] for z in y]

common_help = list(set(x).intersection(set(y)))

##Positive vs negative
x = Counter(" ".join(reviews[pos]["reviews.clean"]).split()).most_common(100)
y = Counter(" ".join(reviews[~pos]["reviews.clean"]).split()).most_common(100)

x = [z[0] for z in x]
y = [z[0] for z in y]

common = list(set(x).intersection(set(y)))
common.extend(x for x in common_help if x not in common)

stop.update(common)

newwords = ["im", "ive", "lik", "like", "unlike", "want", "wanted", "liv",
            "amazing", "excellent", "pleased", "basic", "basically", "highly",
            "thing", "hey", "awesome", "around", "tried", "looking", "likes",
            "pretty", "wouldnt", "dont", "super"]

stop.update(newwords)
reviews["reviews.clean"] = reviews["reviews.clean"].str.split(' ').apply(lambda x: ' '.join(k for k in x if k not in stop))

##WordCloud
##Overall cloud
wc = WordCloud(stopwords=stop, background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42)

text = reviews["reviews.clean"]
text = text.dropna()
text

wordcloud = WordCloud().generate(str(text))

plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()

##Helpful vs Unhelpful wordclouds
text = reviews[helpful_revs]["reviews.clean"]
text = text.dropna()
text

wordcloud = WordCloud().generate(str(text))

plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()

###Unhelpful
text = reviews[~helpful_revs]["reviews.clean"]
text = text.dropna()
text

wordcloud = WordCloud().generate(str(text))

plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()

##Rating comp
###Positive
text = reviews[helpful_revs]["reviews.clean"].where(reviews["reviews.rating"] >= 3)
text = text.dropna()
text

wordcloud = WordCloud().generate(str(text))

plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()

###Negative
text = reviews[helpful_revs]["reviews.clean"].where(reviews["reviews.rating"] <= 3)
text = text.dropna()
text

wordcloud = WordCloud().generate(str(text))

plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()
