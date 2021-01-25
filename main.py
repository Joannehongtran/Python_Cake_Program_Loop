"""
**********************************************************************************
Filename:           Cake_Program

Author:             Joanne Tran

Date:               2020.11.24

Modifications:

Description:        This module creates a Cake class with specific attributes
                    It's tasks includes:
                    1) Creating a class titled Cake to test individual Cake Types
                    2) Define recipe, cake type, name, size, weight, and ingredient list
                    3) Call the defined functions to build the list

************************************************************************************
"""


class Cake:
    cake_type = ["chocolate_cake", "red_velvet_cake", "lemon_cake"]

    recipe = {"chocolate_cake": {"Flour": 15.8, "Sugar": 24.5, "Unsweetened Cocoa Powder": 5.6, "Baking Powder": 0.4,

                                 "Baking Soda": 0.6, "Salt": 0.4, "Egg": 9, "Buttermilk": 18.0, "Canola Oil": 8.1,

                                 "Vanilla Extract": 0.6, "Boiling Water": 17.0},

              "red_velvet_cake": {"Flour": 22.4, "Sugar": 22.4, "Baking Soda": 0.7, "Salt": 0.4,

                                  "Unsweetened Cocoa Powder": .4, "Canola Oil": 24, "Buttermilk": 17.9, "Egg": 9.0,

                                  "Red Food Coloring": 2.1, "Vanilla Extract": 0.3, "Distilled Vinegar": 0.3},

              "lemon_cake": {"Butter": 8.5, "Sugar": 15.0, "Egg": 9.0, "Sifted Self-Rising Flour": 15.6,

                             "Buttermilk": 9.0, "Vanilla Extract": 0.2, "Egg Yolk": 17.9, "SugarF": 11.3,

                             "ButterF": 2.1, "Lemon Juice and Zest": 11.4}}

    filling = {"lemon_cake": ["ButterF", "Lemon Juice and Zest", "SugarF", "Egg Yolk"]}

    # Methods:

    """
    **********************************************************************************
    Function:           def __init__()

    Parameters:         None

    Inputs:             None 

    Outputs:            define self, type, and size while specifying format 

    Returns:            None 

    Author:             Joanne Tran

    Date:               2020.11.24

    Modifications: 

    Description:        This function defines the self, type, and size of the different cakes.
                            It's tasks includes:
                            1) Defining the self, type, and size for the 3 cakes and an ingredient list 
                            2) Defining lists for the cake types 
    ************************************************************************************
    """

    def __init__(self, type, size):

        self.type = type

        self.size = size

        self.name = ""

        self.weight = 0.0

        self.ingrd_list = []

    """
    **********************************************************************************
    Function:           def calc_ingrd()

    Parameters:         cake_wt

    Inputs:             None 

    Outputs:            define and calculate each ingredient in terms of oz 

    Returns:            None 

    Author:             Joanne Tran

    Date:               2020.11.24

    Modifications: 

    Description:        This function calculates the weight of each ingredient and formats in oz.
                        It's tasks includes:
                        1) Check the value of every parameter regarding every ingredient 
                        2) Calculate the total weight for each ingredient 
    ************************************************************************************
    """

    def calc_ingrd(self, weight, recipe):

        self.ingrd_list.append(list(recipe.keys()))

        wt_list = []

        for key in self.ingrd_list[0]:
            amount = float((weight * float(recipe[key]) * 16 / 100))

            wt_list.append(amount)

        self.ingrd_list.append(wt_list)

    """"
    **********************************************************************************
    Function:            def print_ingrd()               

    Parameters:          flour_wt
                         sugar_wt
                         unsweetened_cocoa_powder_wt
                         baking_powder_wt
                         baking_soda_wt
                         salt_wt
                         egg_wt
                         buttermilk_wt
                         oil_wt
                         vanilla_extract_wt
                         boiling_water_wt
                         red_food_Coloring_wt
                         distilled_vinegar_wt
                         butter_wt
                         sifted_self_risng_flour_wt
                         fill_egg_yolk_wt
                         fill_sugar_wt
                         fill_butter_wt
                         fill_lemon_zest_wt

    Inputs:              None

    Outputs:             print the ingredient list in terms of oz with their respectful weight by calling function

    Returns:             None

    Author:              Joanne Tran

    Date:                2020.11.24

    Modifications:

    Description:         This function prints the list and weight of each ingredient in oz.
                         It's tasks includes:
                         1) Check the weight of every parameter regarding every ingredient
                         2) Calculate the total weight for each ingredient 
                         3) Print the total weight 
    ************************************************************************************
    """

    def print_ingrd(self, ingrd_list, ingrd_names):

        for i in range(len(ingrd_names)):
            print("%s : %.1f Oz" % (ingrd_names[i], round(ingrd_list[1][i], 1)))

    def __str__(self):

        ret_str = "\nIngredient Quantities for {} {}\n\n"

        recipe = ""

        size_ind = ""

        if self.type == 3:

            recipe = "Lemon Cake"



        elif type == 2:

            recipe = "Red Velvet Cake"



        else:

            recipe = "Chocolate Cake"

        if self.getSize() == 'L':

            size_ind = "Large"

        elif self.getSize() == 'R':

            size_ind = "Regular"

        ret_str = ret_str.format(size_ind, recipe)

        self.calc_ingrd(self.weight, Cake.recipe[Cake.cake_type[self.type - 1]])

        for i in range(len(self.ingrd_list[0])):

            if self.ingrd_list[0][i] in Cake.filling[Cake.cake_type[self.type - 1]]:

                if self.ingrd_list[0][i].endswith("F"):

                    ret_str += "{} : {:.1f} Oz\n".format(
                        "Filling - " + self.ingrd_list[0][i][:len(self.ingrd_list[0][i]) - 1], self.ingrd_list[1][i])

                else:

                    ret_str += "{} : {:.1f} Oz\n".format("Filling - " + self.ingrd_list[0][i], self.ingrd_list[1][i])

            else:

                ret_str += "{} : {:.1f} Oz\n".format(self.ingrd_list[0][i], self.ingrd_list[1][i])

        return ret_str

    def getType(self):

        return self.type

    def getName(self):

        return self.name

    def getSize(self):

        return self.size

    def getWeight(self):

        return self.weight

    def setData(self, type, size, name, weight):

        self.type = type

        self.size = size

        self.name = name

        self.weight = weight


# Creating the test codes to instantiate cake objects for each type of cake and size (3 types of cake and 2 weights for each)

my_lrg_lemon_cake = Cake(3, 'L')

print(my_lrg_lemon_cake)

my_reg_lemon_cake = Cake(3, 'R')

print(my_reg_lemon_cake)

# Defining ingredient lists for the cake types and weights
# Chocolate = 1, Red velvet = 2, Lemon = 3

recipe_cake = {"chocolate_cake": {"Flour": 15.8, "Sugar": 24.5, "Unsweetened Cocoa Powder": 5.6, "Baking Powder": 0.4,

                                  "Baking Soda": 0.6, "Salt": 0.4, "Egg": 9, "Buttermilk": 18.0, "Canola Oil": 8.1,

                                  "Vanilla Extract": 0.6, "Boiling Water": 17.0},

               "red_velvet_cake": {"Flour": 22.4, "Sugar": 22.4, "Baking Soda": 0.7, "Salt": 0.4,

                                   "Unsweetened Cocoa Powder": .4, "Canola Oil": 24, "Buttermilk": 17.9, "Egg": 9.0,

                                   "Red Food Coloring": 2.1, "Vanilla Extract": 0.3, "Distilled Vinegar": 0.3},

               "lemon_cake": {"Butter": 8.5, "Sugar": 15.0, "Egg": 9.0, "Sifted Self-Rising Flour": 15.6,

                              "Buttermilk": 9.0, "Vanilla Extract": 0.2, "Egg Yolk": 17.9, "SugarF": 11.3,

                              "ButterF": 2.1, "Lemon Juice and Zest": 11.4}}

chocolate_ingredient_list = ["Flour", "Sugar", "Unsweetened Cocoa Powder", "Baking Powder", "Baking Soda", "Salt",

                             "Egg", "Buttermilk", "Canola Oil", "Vanilla Extract", "Boiling Water"]

red_ingredient_list = ["Flour", "Sugar", "Baking Soda", "Salt", "Unsweetened Cocoa Powder", "Canola Oil", "Buttermilk",

                       "Egg", "Red Food Coloring", "Vanilla Extract", "Distilled Vinegar"]

lemon_ingredient_list = ["Butter", "Sugar", "Egg", "Sifted Self-Rising Flour", "Buttermilk", "Vanilla Extract",

                         "Filling\nEgg Yolk", "Sugar", "Butter", "Lemon Juice and Zest"]

cake_wt = 0

cake_type = input('Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ')

while not (cake_type == "q" or cake_type == "Q"):

    cake_wt_type = input("Please select cake size; Enter L for large, R for regular: ")

    if cake_wt_type == 'L':

        cake_wt = 7

        print("Large", end=" ")

    elif cake_wt_type == 'R':

        cake_wt = 4

        print("Regular", end=" ")

    else:

        print("Wrong input")

    if cake_type == '1':

        cake = Cake(cake_type, cake_wt)

        cake.calc_ingrd(cake_wt, recipe_cake['chocolate_cake'])

        ingrd_liste = cake.ingrd_list

        ingrde_names = chocolate_ingredient_list

        # print ingrde_names

        print("Chocolate Ingredient List: ")

        cake.print_ingrd(ingrd_liste, ingrde_names)

    elif cake_type == '2':

        cake = Cake(cake_type, cake_wt)

        cake.calc_ingrd(cake_wt, recipe_cake['red_velvet_cake'])

        ingrd_liste = cake.ingrd_list

        ingrde_names = red_ingredient_list

        # print ingrde_names

        print("Red Velvet Ingredient List: ")

        cake.print_ingrd(ingrd_liste, ingrde_names)

    elif cake_type == '3':

        cake = Cake(cake_type, cake_wt)

        cake.calc_ingrd(cake_wt, recipe_cake['lemon_cake'])

        ingrd_liste = cake.ingrd_list

        ingrde_names = lemon_ingredient_list

        # print ingrde_names

        print("Lemon Ingredient List: ")

        cake.print_ingrd(ingrd_liste, ingrde_names)

    cake_type = input('Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ')