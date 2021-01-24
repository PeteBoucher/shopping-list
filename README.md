# shopping-list

## Lesson 1
Output a list
### Section 1
Create a shopping list and let pyton print it to the command line
1. Create a List and populate it with the fruit and veg Mum needs in this weeks shopping trip.
2. Define a function to print out the list to the command line and call it from `__main__`
3. Run the app `python3 main.py`
4. Output should be `['EGGS X24', 'FRUIT', 'BANANAS', 'BERRIES', 'CUCUMBERS', 'LETTUCE', 'SQUASH (1/2)', 'MUSHROOMS', 'POTS', 'ASPARAGUS X2', 'LEEKS', 'SWEET POTS', 'FRESH PINEAPPLE', 'TOMS']`
`
### Section 2
1. Import Flask and use pip to install it `pip3 install flask`
2. Follow the [Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/) example in the Flask docs to create 
and test a simple flask page
3. Replace the `hello_world` function with one that outputs your list to the page as a string using `''.join(shopping_list)`
4. Observe output is not readable, all the items are smooshed together in one line
5. Modify the function to  build an `output` String from the list as an unordered list `<ul>` in HTML
### Bonus activity
6. Commit your code to git `git init && git commit -m 'initial shopping list flask app'`
7. Push to a public repo `git remote add origin [MY_REPO] && git push`