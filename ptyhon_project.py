# -*- coding: utf-8 -*-
import pandas as pd
import random
import numpy as np

"""
this program is designed to get the user thinking about the issues of
online privacy. Companies collect all kinds of data on users, from the obvious
that you give when you make the account to the hidden data that is colected
on your behavior. This program begins by asking the user to create an account
to get started even thoug it is not necissery for the program function. Many
websites and services requier people to create accounts to colect as much data
as possible.

"""

def main():
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
      sexual orientation, ethnicity, religious and political views, personality traits, intelligence, happiness, use of addictive substances, parental separation, age, and gender''' , '''
      The model correctly discriminates between homosexual and heterosexual men in 88% of cases,
      African Americans and Caucasian Americans in 95% of cases, and between
      Democrat and Republican in 85% of cases''']

            for element in facts:
                  print element + '\n'
                  raw_input("Press Enter to continue...")


      """
      tests the users knowledge based on what they learned previousley in the program.

      """
      def quiz():
            pass




      """
      something a little more personal
      """
      def personal():
            """ imports and reads a csv file containign tweets"""
            df = pd.read_csv('realDonaldTrump_tweets.csv', encoding = 'iso-8859-1')

            ''' removes all the retweeets'''
            nort = df[df['Tweet Type'] == "Tweet"]

            ''' finds the most popular post based on retweets and prints result'''
            nort = nort.set_index("Retweets").sort_index(ascending=False)
            print nort.head(1)['Text']

            ''' finds the most popular post based on favorites and prints result'''
            nort = nort.set_index("Favorites").sort_index(ascending=False)
            print nort.head(1)['Text']

            ''' randomly prints tweets and the username'''
            for _ in range(5):
                  print(np.random.choice(nort['Text']+ ' @'+ nort['Screen Name'] + '\n' ))
      info()
      learn()
      personal()

main()
