# Brittany DiFede
# Pledge: I pledge my honor that I have abided by the Stevens Honor System -BD
# EE 551 Final Project: K nearest neighbors implementation
import pandas as pd
import math as mt
import random

# Calculate euclidean distance
def euclidean(x1, x2):
    distance = 0.0
    distance += (x1 - x2) ** 2
    return mt.sqrt(distance)


# Given a list of attributes it returns 10 random ones
def attribute_return(lis):
    return random.sample(lis, 10)


k = 3
# Read in csv
df = pd.read_csv('movies.csv')
# print(df)
# Create training and testing datasets
train_set = df.sample(frac=0.8, random_state=0)
test_set = df.drop(train_set.index)
best_run = 0
best_attributes = []
for counters in range(100):
    attributes =list(df.columns.values[6:])
    attributes = attribute_return(attributes)

    # attributes = attribute_return()
    train_set_values = train_set.loc[:, attributes]
    test_set_values = test_set.loc[:, attributes]
    # print(test_set_values)


    count = 0
    distance = 0
    distances = []
    for y in range(len(test_set_values)):
        for x in range(len(train_set_values)):
            distance = 0
            for i in range(len(attributes)):
                movie = {}
                movie["title"] = train_set.iloc[x][0]
                movie["genre"] = train_set.iloc[x][1]
                distance += euclidean(test_set_values.iloc[y][i], train_set_values.iloc[x][i])
                movie["distance"] = distance
                distances.append(movie)
        distances = sorted(distances, key=lambda k: k["distance"])
        action = 0
        romance = 0

        for i in range(k):
            if distances[i]["genre"] == "action":
                action += 1
            else:
                romance += 1
        if action > romance:
            if test_set.iloc[y][1] == "action":
                # print('got one right')
                count += 1
        else:
            if test_set.iloc[y][1] == "romance":
                count += 1
                # print('got one right')

    percent_correct = count / len(test_set)
    if percent_correct > best_run:
        best_run = percent_correct
        best_attributes = attributes
    print("Percent correct with k:" + str(k) + ": ")
    format_float = "{:.3f}".format(percent_correct)
    print(format_float)
    print("Current iteration " + str(counters))

print(best_attributes)
print(best_run)
