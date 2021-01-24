# Python program to manage the Mercadona shop
from flask import Flask

app = Flask(__name__)

shopping_list = ["EGGS X24",
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


@app.route('/')
def index():
    output = "<ul>"
    for item in shopping_list:
        output += "<li>" + item + "</li>"
    output = output + "</ul>"
    print(output)
    return output


def print_shopping_list():
    print(shopping_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
