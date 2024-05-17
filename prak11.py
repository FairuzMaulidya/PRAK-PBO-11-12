# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:33:13 2024

@author: Fairuz Maulidya
"""

class FullNameDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, title, first_name, last_name, nim):
        full_name = self.func(title, first_name, last_name, nim)
        return f"Full Name {full_name}"

@FullNameDecorator
def generate_full_name(title, first_name, last_name, nim):
    return f"{title} {first_name} {last_name} {nim}"

title = "Ms."
first_name = "Fairuz"
last_name = "Maulidya"
nim = "064002300018"

print(generate_full_name(title, first_name, last_name, nim))
