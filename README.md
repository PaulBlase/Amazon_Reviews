# Amazon Reviews

## Dataset
This dataset provides a set of 34.7 thousand reviews of the Amazon Kindle, Fire Stick, and other products. Provided by Datainfiniti's Product Base, it was made available through Kaggle (https://www.kaggle.com/datafiniti/consumer-reviews-of-amazon-products).

While there are a multitude of different reviews posted on different products, which reviews provide the most value? In this assessment I hope to analyze what is written in a valuable review and what those reviews detail as true. In order to assess this, from the initial dataset, we will analyze the text in the title and review, the number of helpful ratings, and the review's rating of the product. 

## Initial Assessment of Reviews
![helpful_rev](https://user-images.githubusercontent.com/40553610/61302219-67903780-a7b3-11e9-8a11-39d3dd06ac83.jpeg)

First, reviews are broken down into helpful (being marked as helpful by at least one other customer) or unhelpful. Based on missing values, we do not have a mark for helpfulness on 529 reviews. These will be deemed as unhelpful, receiving a zero mark for the numeric value. The remaining observations with missing values are removed, leaving a total of 34,621 observations.

This leaves us with a total of 3,309 reviews deemed helpful. These reviews, broken down by rating, are listed below:

![help_map](https://user-images.githubusercontent.com/40553610/61257799-8f928300-a740-11e9-8c2c-b1b99e11170c.jpeg)![help_map1](https://user-images.githubusercontent.com/40553610/61257810-9a4d1800-a740-11e9-938a-77fc5d45397f.jpeg)

We see that the majority of reviews received about Amazon products are positive. However, lower ratings are consistent with a higher percentage of helpful reviews, possibly because they critque specific elements more thoroughly and also being that they stand out from the multitude of more positive reviews.

In analyzing the text, we struggle to distinguish trends from the data the truly differentiate the helpful and unhelpful reviews from each other. Often we find a trend in the distribution plots that match this, highlighting the number of characters in a review text.

![helpful_char](https://user-images.githubusercontent.com/40553610/61308844-19813100-a7bf-11e9-8bd6-cad0c1f71869.jpeg)

However, when assessing the title text, we do see one identifier. In helpful reviews, generally we see at least one capitalized character and no more than three. Assuming that unhelpful reviews are emotionally charged, that might lead to someone capitalizing characters excessively and could be a quick rule of thumb to assess review quality.

![helpful_uptitle](https://user-images.githubusercontent.com/40553610/61309030-7bda3180-a7bf-11e9-96fa-8d782f75970f.jpeg)

## Subjectivity and Polarity

## Wordclouds
In order to better assess specific elements of the reviews, stop words were removed and wordcloud modeling was done to assess the main topics of the user reviews as a whole.

![wordcloud_crop](https://user-images.githubusercontent.com/40553610/61241436-7d4d2080-a711-11e9-959f-26ae311decdc.jpeg)

From this initial point, reviews were broken down into helpful and unhelpful reviews. From there, similar words were assessed the an updated stop words list and removed. In addition, words that did not really define specifically value or detrimental parts of the Kindle (specifically adjectives like "excellent" or "bad") were removed to pinpoint clearer talking points.

Assessing differences between helpful and unhelpful reviews, these were the wordclouds for the separate datasets:

Helpful | Unhelpful
:-------------------------:|:-------------------------:
![wordcloud_help1_crop](https://user-images.githubusercontent.com/40553610/61241548-b7b6bd80-a711-11e9-9013-e3d6d1975d86.jpeg) | ![wordcloud_unhelp1_crop](https://user-images.githubusercontent.com/40553610/61241777-34e23280-a712-11e9-9f42-2882d621c3b6.jpeg)

We see with the helpful reviews, there is a focus on price point as well as the graphics. In assessing ratings based wordclouds, we will see these are generally elements discussed in positive reviews. However, on the unhelpful side, there is discussion about some of the hardware, such as chargers and usb ports. Also, there is mention of words possibly citing the individual as less tech-savvy (library, mentioning computer or monitors with tablets, etc.).

From here we look at the difference between positive and negative reviews, taking from the helpful reviews:

Positive | Negative
:-------------------------:|:-------------------------:
![wordcloud_pos1_crop](https://user-images.githubusercontent.com/40553610/61242404-9b1b8500-a713-11e9-8ce0-a91d189b0faf.jpeg) | ![wordcloud_neg1_crop](https://user-images.githubusercontent.com/40553610/61242425-a40c5680-a713-11e9-9353-f85ba2f159b1.jpeg)

On the positive side, as we had seen in helpful overall, there's mention of the graphics quality, as well as terms referencing the value of the product. It seems that, with cable being mentioned often, that those purchasing Amazon products were looking to cut the cord and that several are satisfied with using them to replace their TV service. 

With some mention of the sound, it seems overall customers find the Kindle to be well priced and offers good features for watching videos and viewing elements, such as articles from the internet. While not in the boardroom during the process, it seems that this is what the product is advertised as and meets expectations.

With negative reviews, however, the few hundred reviews spoke to the somewhat inconsistent quality of the product. With wording indicating recurring technical issues, such as "several", "problem", "issue", "kept", and "multiple", there's probably a case to be made that more support for the customers could allow the product to offer more value. This could be due to interactions with applications, with Roku, FireTv, and Netflix all being mentioned. This would suggest that applications setup for the device experience bugs and should be monitored more frequently to ensure higher quality. 

There's also discussion of internet connection and wifi along with the use of "model" and "upgrade" as two of the most common words. This is likely suggesting that, as with most budget tech, not everything is guarenteed to work with your first model and issues with the wifi will likely be something tech support will deal with frequently.

While there seem to be some issues on both the software and hardware side of Amazon products, the overall sentiment is positive. As we see, for the price of the unit, the display and sound are worth the money for those looking for a budget tablet. 
