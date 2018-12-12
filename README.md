# YouTube Video Comments

End of semester Python MapReduce challenge

## Link

<https://bitbucket.org/professorcase/h14>

## Introduction

The dataset includes data gathered from video comments on YouTube from the trending category each day.

## Data Source

The data source is structured data in a csv file in the following format:

video_id,comment_text,likes,replies

XpVt6Z1Gjjo,"Logan Paul it's yo big day ‼️‼️‼️",4,0

XpVt6Z1Gjjo,"I've been following you from the start of your vine channel and have seen all 365 vlogs",3,0

XpVt6Z1Gjjo,"Say hi to Kong and maverick for me",3,0

XpVt6Z1Gjjo,"MY FAN . attendance",3,0

XpVt6Z1Gjjo,"trending 😉",3,0

XpVt6Z1Gjjo,"#1 on trending AYYEEEEE",3,0

XpVt6Z1Gjjo,"The end though 😭👍🏻❤️",4,0

## Big Data Challenge

For each video, find the count of comments.

## Big Data Solution

1. Write a mapper named vmapper.py

2. Write a sorter named vsorter.py

3. Write a reducer named vreducer.py

4. Open Excel. Use Data / Import to bring in the results of your reducer. Use Data/ Filter / Sort to find highest count.

## Many Thanks to Original Sources

<https://www.kaggle.com/datasnaek/youtube>
44-564 Spring 2018 Group 2C
