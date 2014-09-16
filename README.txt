Name - Thejas.R
USN - 1PI12IS120
Ques No - 5
Question Title - You are given a .csv file which has been written in the following format COUNTRY,CAPITAL,POPULATION
Write a program which reads data from the .csv file and populates it into a .txt file in the form of sentences like:
The capital of <COUNTRY> is <CAPITAL> with a population of <POPULATION>.
This application has a new requirement to display the most spoken language of that country. Add 
another column called LANGUAGE in the csv file such that the order looks like this: 
 
COUNTRY,CAPITAL,POPULATION,LANGUAGE 
and it should populate into the .txt file should be in the form of the following sentences: 
 
The capital of <COUNTRY> is <CAPITAL> with a population of <POPULATION> and the 
language spoken is <LANGUAGE> 
 
Source Code Files-
assign3.py - This file contains the program written to execute the problem statement
countries.csv - This file consists of a collection of four columns (country,capital,population and Language) of various countries

Copy both these files to the same directory and in command line cd to that folder
type in python3 assign3.py -f <file_name> -l <logfile_name>

Bugs - It doesnt handle cases where in you compile the program without command line arguments 