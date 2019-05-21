# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:32:55 2019

@author: mmelkowski
"""

import pandas as pds

class stat_primes:
    def __init__ (self, fname="primes.txt"):
        self.prime_dataframe = pds.DataFrame([[0,0,0,0],
                                              [0,0,0,0],
                                              [0,0,0,0],
                                              [0,0,0,0]])

        self.prime_dataframe.rename(columns={0:'1', 1:'3', 2:'7', 3:'9'},
                                    inplace=True)
        self.prime_dataframe.rename(index={0:'1', 1:'3', 2:'7', 3:'9'},
                                    inplace=True)
        
        #load
        f = open(fname,"r")
        self.primes_values = f.readlines()
        f.close()


    def clean_primes(self):
        self.primes_values = [elt.strip() for elt in self.primes_values]
        self.primes_values = self.primes_values[3:]


    def count_primes(self):
        i=1
        val = self.primes_values[i-1][-1]
        while i < len(self.primes_values):
            follow = self.primes_values[i][-1]
            self.prime_dataframe.at[val, follow] += 1
            val = follow
            i+=1


    def mean_primes(self):
        self.prime_dataframe = self.prime_dataframe.T
        for col in self.prime_dataframe.columns:
            self.prime_dataframe[col] = round((self.prime_dataframe[col]/
                                               self.prime_dataframe[col].sum()
                                               )*100,2)
        self.prime_dataframe = self.prime_dataframe.T
"""
stat = stat_primes()
stat.clean_primes()
stat.count_primes()
stat.mean_primes()
"""
