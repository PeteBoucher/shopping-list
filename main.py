# Python program to manage the Mercadona shop
from flask import Flask, render_template

app = Flask(__name__)

fruit_and_veg = ["EGGS X24",
                 "FRUIT",
                 "BANANAS",
                 "BERRIES",
                 "CUCUMBERS",
                 "LETTUCE",
                 "SQUASH (1/2)",
                 "MUSHROOMS",
                 "POTS",
                 "ASPARAGUS X2",
                 "LEEKS",
                 "SWEET POTS",
                 "FRESH PINEAPPLE",
                 "TOMS"]
meat = ["MINI BURGERS", "CHICKEN BREAST"]
shopping_list = [meat, fruit_and_veg]


@app.route('/')
def index():
    return render_template('list.html', list=shopping_list)


def print_shopping_list():
    print(shopping_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
