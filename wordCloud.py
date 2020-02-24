import matplotlib.pyplot as plt
from wordcloud import WordCloud

content = "All of this is a random bunch of words none of this make any sense except for the purpose of creating a world cloud"

cloud = WordCloud(background_color="orange").generate(text)
plt.axis('off')
plt.imshow(cloud)
plt.show()
