# Conference-Paper-Recommendation-System-using-LSH

Recommender systems help the users to get personalized recommendations and redefine the users web browsing experience. \
For large data, a faster and scalable algorithm is required. \
Hence, Locality Sensitive Hashing (LSH) is used as a criterion to find the similarity between conference papers. 

Dataset source: https://www.kaggle.com/paultimothymooney/cvpr-2019-papers 

#### Preprocessing Steps:
- Lowercase all text.
- Remove all digits.
- Remove all punctuations.
- Removing stop words.
- Lemmatization (Stemming).

#### Implementation

- Reading the document data as a single dictionary
- Converting the document into a set of k-shingles
- Generate Minhash Signatures
- Compute True Jaccard Similarity and find top-n similar documents.
-  Compute Estimated Jaccard Similarity using the Signature Matrix and find top-n similar documents.
- Compare the recommendations provided by True and estimated Jaccard Similarity.
- In LSH, we find  appropriate b and r values to find most similar pair of documents.
- Obtain TP and FP values to evaluate LSH.

<img src="Time_Consumption.png" height="250" /> \
<img src="Comparison.png" height="150" /> 
\
<img src="Time_Analysis.png" height="250" />

Thus, LSH provides good accuracy and is highly efficient in recommending conference papers.

