# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:32:55 2019

@author: mmelkowski
"""

class supermarket():
    def __init__(self, a, o, w):
        self.price_apple = 0.20
        self.price_orange = 0.50
        self.price_watermelon = 0.8

        self.nb_apple = a
        self.nb_orange = o
        self.nb_watermelon = w
        
        self.price_basket()

    def apply_sales(self, nb,x,y):
        """
        sale = x apple for the price of y
        """
        return (nb//x)*y + nb%x

    def price_basket(self):
        #set up sale a la main, need automat
        self.nb_apple = self.apply_sales(self.nb_apple, 2, 1)
        self.nb_watermelon = self.apply_sales(self.nb_watermelon,3,2)

        p_apple      = self.nb_apple      * self.price_apple
        p_orange     = self.nb_orange     * self.price_orange
        p_watermelon = self.nb_watermelon * self.price_watermelon

        print(sum([p_apple, p_orange, p_watermelon]))


if __name__ == "__main__":
    s = supermarket(4,3,5)

