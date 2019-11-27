# -*- coding: utf-8 -*-
import pandas as pd
import random
import numpy as np
import sys
import csv
from collections import Counter

"""
this program is designed to get the user thinking about the issues of
online privacy. Companies collect all kinds of data on users, from the obvious
that you give when you make the account to the hidden data that is colected
on your behavior.  This program begins by asking the user to create an account
to get started even thoug it is not necissery for the program function. Many
websites and services requier people to create accounts to colect as much data
as possible. Another main aspect of this programm is for to view twitter post data
has been colected, they can view the most popular tweet of an account based on
favorites or retweets, or view 10 random tweets. This shows the user how easy it
can be to get and then manipulate their personal data. It is very easy to change the
csv data file to be of a particular user.


"""

def main():

      ''' prints welcome message'''

      print(
            '''
            =======================================
            |                                     |
            |                                     |
            |  WELCOME TO A WORLD WITHOUT PRIVACY |
            |                                     |
            |                                     |
            =======================================
            ''')

      raw_input("Press Enter to continue...")


      """
      Has user imput information and create and account, this is neccessary to continue
      in the program even though the data itself is not necessary. This is done to emulate
      companies that force you to make an account to use a service even if in reality that is not necessary
      """
      def info():

            print 'Before we begin please enter some information to create your account'
            name = raw_input('Enter your name: ')
            print name
            email = raw_input('Enter your email: ')
            phone = raw_input('Enter your phone number: ')
            age = raw_input('Enter your age: ')
            gender = raw_input('Enter your gender: ')
            username = raw_input('Create a username: ')
            password = raw_input('Create a password: ')
            print 'Welcome ' + name
            print 'thank you for creating an account, you may now proceed to the rest of the program'
      '''
      forces the to create an account, like many websites such as pintrest that do
      not lat you usee their service without an account. They do this to collect user data
      so they can sell ads
      '''
      print 'Before you can continue you must create an account'
      print '1: Create an account'
      print '2: Exit'
      x = raw_input(": ")
      if x == '1':
            info()
      elif x == '2':
            sys.exit()
      choice = ''

      while choice != '3':


            """
            teaches the user about the issues on online privacy
            provides facts and staristics
            prevelence of data breeches
            how much data can be worth
            how it is used
            """
            def learn():
                  facts = ['21% of online users are the victim of account hacking ', '11% of online users have been the victim of data theft',
                           '12% of online users are the victim of cyberstalking and spying',
                           '''Estimates are that the big four (Google, Amazon, Microsoft and Facebook
                           store at least 1,200 petabytes between them. That is 1.2 million terabytes''',
                           '''Facebook has about 190 million users in the U.S., so we estimate that Facebook can make
            between $38 million and $76 million from selling such data points on American users''', '''Facebook likes can help predict a user’s
            sexual orientation, ethnicity, religious and political views, personality traits,
            intelligence, happiness, use of addictive substances, parental separation, age, and gender''', '''The model correctly discriminates
            between homosexual and heterosexual men in 88% of cases, African Americans and Caucasian Americans in 95% of cases, and between
            Democrat and Republican in 85% of cases''']

                  for element in facts:
                        print element + '\n'
                        raw_input("Press Enter to continue...")

            """
            takes twitter data of a particular user which has been gathered in a csv file and allowes the user to view difrent
            aspects of it like a random tweet, most retweeted, most liked and most common words

            """
            def personal():
                # creates list of file options
                  tweetList = ["Zebradontcare_tweets.csv", "jamesjbrownjr_tweets.csv", "realDonaldTrump_tweets.csv"]

                  print 'whose tweets would you like to view?'
                  #lets the user chose whose tweets they want to view
                  for i in range(len(tweetList)):
                        print("{}: @{}".format(i+1, tweetList[i].split('_')[0]))

                #imports and reads a csv file containign tweets"""
                  selection = int(raw_input("Choose an option: "))
                  df = pd.read_csv(tweetList[selection-1])

                  ''' removes all the retweeets'''
                  nort = df[df['Tweet Type'] == "Tweet"]

                #gives the user a lost of options
                  print 'What would you like to do?'
                  print '1: View the most popular post based on retweets'
                  print '2: View the most popular post based on favorites'
                  print '3: View 10 random tweets'
                  option = raw_input("Choose an option: ")

                  if option == '1':
                        ''' finds the most popular post based on retweets and prints result'''
                        nort = nort.set_index("Retweets").sort_index(ascending=False)
                        print "Most popular tweet (RTs):\n{}".format(nort.values[0][1])

                  elif option == '2':
                        ''' finds the most popular post based on favorites and prints result'''
                        nort = nort.set_index("Favorites").sort_index(ascending=False)
                        print "Most popular Tweet (liked):\n{}".format(nort.values[0][1])

                  elif option == '3':
                        ''' randomly prints tweets and the username'''
                        for _ in range(10):
                              print(np.random.choice(nort['Text']+ ' @'+ nort['Screen Name'] + '\n' ))

            ''' gives the user a choice of what to do'''
            print '\n'
            print 'What would you like to do: '
            print '1: learn about online privacy'
            print '2: view personal tweets'
            print '3: Exit'

            ''' asks for user input and then proceds to the apropriate part of the program'''
            choice = raw_input("Choose an option: ")
            if choice == '1':
                  learn()
            elif choice == '2':
                  personal()
            elif choice == '3':
                # exits the program
                  print 'Thank you for participating'
                  sys.exit()


main()
