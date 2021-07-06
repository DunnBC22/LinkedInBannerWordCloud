# Source: Duong Vu (https://www.datacamp.com/community/tutorials/wordcloud-python)

import re
import pandas as pd
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# %matplotlib inline

terms = []

with open('/Users/briandunn/Data Analysis/wordcloud/WordsToInclude.txt', 'r') as file:
    terms = file.readlines()

wordcloud = WordCloud(background_color="#429bb8", width=1584, height=396).generate(' '.join(terms))
# Generate the plot
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
plt.draw()

# output the image
wordcloud.to_file("/Users/briandunn/Documents/Output2.png")
