# Game Of Throne

Coding challenge for insight data engineering program

## Introduction

Calculate inverted index for words given a list of files.

Consider a 2 files given

**File 1** - *This is a primary file*

**File 2** - *This is a secondary file*

Then to calculate reverse index

1. map elements of the files to a Value

```
  This - 0
  is - 1
  a - 2
  primary - 3
  file - 4
  secondary - 5
```

1. Use the map generated earlier and the files to understand which words lie in which files

```
  0 - [File 1, File 2]
  1 - [File 1, File 2]
  2 - [File 1, File 2]
  3 - [File 1]
  4 - [File 1, File 2]
  5 - [File 2]  
```

## Motivation

Reverse Indexing or block sort based indexing has several use cases

1. The inverted index data structure is a central component of a typical search engine indexing algorithm. A goal of a search engine implementation is to optimize the speed of the query: find the documents where word X occurs. Once a forward index is developed, which stores lists of words per document, it is next inverted to develop an inverted index. Querying the forward index would require sequential iteration through each document and to each word to verify a matching document. The time, memory, and processing resources to perform such a query are not always technically realistic. Instead of listing the words per document in the forward index, the inverted index data structure is developed which lists the documents per word.

1. In bioinformatics, inverted indexes are very important in the sequence assembly of short fragments of sequenced DNA. One way to find the source of a fragment is to search for it against a reference DNA sequence. A small number of mismatches (due to differences between the sequenced DNA and reference DNA, or errors) can be accounted for by dividing the fragment into smaller fragments—at least one subfragment is likely to match the reference DNA sequence. The matching requires constructing an inverted index of all substrings of a certain length from the reference DNA sequence. Since the human DNA contains more than 3 billion base pairs, and we need to store a DNA substring for every index and a 32-bit integer for index itself, the storage requirement for such an inverted index would probably be in the tens of gigabytes.

## Installation and Run

Clone this repository using `git clone `

Run the program using `spark-submit src/reverse_indexing.py --input data/indexing --output output`
