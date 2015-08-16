=============================
Android Apps Reviews Dataset
=============================

There are two files *positive10k* and *negative10k* that conatins positive and negative reviews of some of the top apps of android app store. ID of the apps whose reviews are taken is in the file appsid.

Purpose
++++++++

This data set can be used to make projects that uses suprevised machine learning algorithms and trained the algorithms with this data. Sentiment analysis algorithms requires data to trian and then test the algorithm. 


Crawler
+++++++

This project also conatins a simple python script for crawling the play store apps and string the reviews. So, anyone who wnats to build their own dataset with their custome requirements can modify the *appsid* file and *Androidapp_reviewscrawler.py* files. To reduce the number of requests this crawler make only one request to get the reviews for each app(40 reviews).

For ex:

* Dataset for Communication apps only.
* More reviews etc
