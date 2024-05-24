# Assignment 04

**Group members**
- First member student's name (student ID number) (number of problem that you solve)
- Second member student's name (student ID number) (1)
- Third member student's name (student ID number) (2, 4)
- etc.


## Problem 1
Using a function [`percolation_centrality`](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.percolation_centrality.html) in `networkx` library explores 
the meaning of percolation centrality. You can use the Jupyter notebook file   
`ch-22-network-analysis-02-rand-geo-graphs.ipynb`. Put it into a contrast to other
three centralities that you have learned in the class.
You can read the original paper on this work from [(Piraveenan et al., 2013) - 
Percolation Centrality: Qyuantifying Graph-Theoretic Impact of Nodes during 
in Networks](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0053095).


## Problem 2
Given the following table of actuarial students activities:
[Note: all the coincidences in the names and activites are just purely random number generator]
| name | activities |
|------|------------|
| Desilya    | hiking, cooking, gardening, painting, biking, meditating, running |
| Annisa     | cooking, gardening, writing, birdwatching, visiting               |
| Sabina     | volunteering, dancing, watching, crafting, listening, picknicking |
| Claren     | volunteering, gaming, exercising, hosting, shopping |
| Hadiyyana  | attending, fishing, swimming, hosting |
| Azfa       | reading, yoga, biking, volunteering, gaming, traveling |
| Mazul      | puzzling, exercising, shopping, calligraphy |
| Yahya      | photographing, swimming, stargazing, crafting |
| FourTwoman | hiking, learning, competing, stargazing |
| Auliah     | hiking, painting, biking, knitting |
| Sulindah   | gaming, shopping, picknicking |
| Amanda     | reading, learning, competing, exercising |
| Anriyani   | volunteering, gaming, watching |
| Brema      | gardening, writing, playing, visiting, exploring |
| Sabina     | fishing, hosting, workshoping |


Perform user-based collaborative filtering to find out for a given user what 
is the best recommendation for it.
Test your answer for the user: **FourTwoman**

## Problem 3
Perform JOIN operation for the following three tables:    
[Note: Several names uses romaji and Japanese characters. Choose ONLY one that you are convenient with]
- Table 1: Bands    
  |`id_` | `name_`    |
  |------|--------------|
  | 1    | Jyocho       |
  | 2    | Uchu Konbini (宇宙コンビニ) |
  | 3    | Covet        |
  | 4    | Österreich   |

  
- Table 2: Songs   
  |`id_` | `name_`      | `release_year` | `band_id` |
  |------|--------------|----------------|-----------|
  | 1    | Yasui inochi (安い命) | 2016           | 1         |
  | 2    | Pyramid      | 2013           | 2         |
  | 3    | Hikari no Kagen ni Hanashita (光の加減で話した) | 2014 | 2   |
  | 4    | Kimi o tsurete yuku (きみを連れてゆく) | 2020    | 4         |
  | 5    | Farewell     | 2020           | 3         |
  | 6    | Shibuya      | 2018           | 3         |
  | 7    | Atreyu       | 2020           | 3         |
  | 8    | Hills        | 2017           | 1         | 

- Table 3: Users
  | `id_` | `name_` | `song_id` |
  |-------|---------|-----------|
  | 1     | Yasuke        | 2   |
  | 2     | Arisa         | 2   |
  | 3     | Banach        | 8   |
  | 4     | ThreeInOneMan | 6   |
  | 5     | Banach        | 3   |
  | 6     | Banach        | 4   |
  | 7     | ThreeInOneMan | 7   |
  | 8     | Arisa         | 3   |
  | 9     | Arisa         | 4   |
  | 10    | Banach        | 1   |
  | 11    | Banach        | 5   |
  | 12    | Yasuke        | 3   |
  | 13    | Arisa         | 1   |
  | 14    | Arisa         | 2   |
  | 15    | Arisa         | 8   |

Your query is to get how many users listen to each song (includes also 
the band's name). Be careful with the condition for the user who listen 
the same song more than once. You should count it as one.
Your answer should include the command to insert those three tables and how to get the asked query.
You can add some screenshot in pgAdmin application that your query commands actually works.

## Problem 4
From the following paper [(Brindopke, 2021) - Actuarial Data Science](https://drive.google.com/file/d/1xTHlQpnjesKOrUhTgSKdJtepPJBssmKA), 
get the core ideas what is "Actuarial Data Science" is according to that paper. 
This is not a summary but your thought and comments to that paper.
Are the materials that you have learned during this semester in this Data Science  
course is covered by that paper?  
[Note: I know that you can use chatGPT-like tools, but I hope each student
try to use their brain to read a paper. Without practicing reading an article
your cognitive skill / brain will cease to exist. You can translate the paper, 
but I think it won't improve your English skill. Try to understand each sentence
and then each paragraph and continue to the whole content. When you learn, you gain a skil, and you can trade to other people what you can offer.]