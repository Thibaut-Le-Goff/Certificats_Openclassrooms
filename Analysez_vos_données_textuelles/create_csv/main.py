from gen_csv import *
from datasets import load_dataset

sentient_data_X = load_dataset("DDSC/twitter-sent", split="train")
sentient_data_y = load_dataset("DDSC/twitter-sent", split="test")
# source of the dataset :
# https://huggingface.co/datasets/DDSC/twitter-sent

data_sample = sentient_data_X[0]

print(type(sentient_data_X))
print(data_sample)

from_dataset("text", sentient_data_X, 'feature_X.csv')

"""
with open('../feature_X.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    field = ["text"]
    writer.writerow(field)

    for row in range(len(sentient_data_X)):
        # write a row to the csv file
        writer.writerow([sentient_data_X[row]["text"]])
"""

"""
The emojis, without counting the flags, will propably have to be removed :
exemple :

import demoji
text_with_emojis = "I love Python! 🐍😃"
text_without_emojis = demoji.replace(text_with_emojis, '')
print(text_without_emojis)
"""