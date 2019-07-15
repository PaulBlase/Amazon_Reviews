# Amazon Reviews

## Dataset
This dataset provides a set of 34.7 thousand reviews of the Amazon Kindle, Fire Stick, and other products. Provided by Datainfiniti's Product Base, it was made available through Kaggle (https://www.kaggle.com/datafiniti/consumer-reviews-of-amazon-products).

## Initial Assessment of Reviews

## Subjectivity and Polarity

## Wordclouds
In order to better assess specific elements of the reviews, stop words were removed and wordcloud modeling was done to assess the main topics of the user reviews as a whole.

![wordcloud_crop](https://user-images.githubusercontent.com/40553610/61241436-7d4d2080-a711-11e9-959f-26ae311decdc.jpeg)

From this initial point, reviews were broken down into helpful and unhelpful reviews (helpful meaning at least one other user marked the review as helpful). From there, similar words were assessed the an updated stop words list and removed. In addition, words that did not really define specifically value or detrimental parts of the Kindle (specifically adjectives like "excellent" or "bad") were removed to pinpoint clearer talking points.

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
