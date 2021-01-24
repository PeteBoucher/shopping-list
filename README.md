# shopping-list
At home we have a shared Google sheet where Mum keeps a shopping list of items we need in our next visit to the 
supermarket. Every week we print out the current version of this spreadsheet and take it to our local Mercadona. 
This project is intended to save paper and preparation time by serving the shopping list as a web page that can be

## Lesson 1
Output a list (90 mins)
### Section 1
Create a shopping list and let pyton print it to the command line
1. Create a List and populate it with the fruit and veg Mum needs in this weeks shopping trip.
2. Define a function to print out the list to the command line and call it from `__main__`
3. Run the app `python3 main.py`
4. Output should be `['EGGS X24', 'FRUIT', 'BANANAS', 'BERRIES', 'CUCUMBERS', 'LETTUCE', 'SQUASH (1/2)', 'MUSHROOMS', 'POTS', 'ASPARAGUS X2', 'LEEKS', 'SWEET POTS', 'FRESH PINEAPPLE', 'TOMS']`

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

## Lesson 2
Output the list via an html template
### Section 1
1. Import render_template
2. remove the code from `index()` that builds the html code around the list and simply return the  result of a call to 
render_template() with the template filename and list passed as arguments:
`render_template('list.html', list=shopping_list)`
3. Add a templates/ folder and a list.html file
4. follow the example on [Jinja2 docs](https://jinja.palletsprojects.com/en/2.11.x/templates/) to iterate over the list
to build the `<ul>` unordered list html.

### Bonus activity
1. Configure Flask in debug mode so that you dont have to break and restart the server after every code edit:
`export FLASK_DEBUG=true`

### Section 2
Mums list has more than just Fruit and Veg, there are other sections. We should have them all shown on the page.
1. remane the `shopping_list` variable to `fruit_and_veg`
2. add a new List for the meat section called `meat`
3. create a new List of Lists called `shopping_list` and populate it with fruit_and_veg and meat:
`shopping_list = [meat, fruit_and_veg]`
4. observe both lists are shown on the page but inline as 2 items
5. update the template to create nested unordered lists for each section
```html
<ul>
    {% for section in list %}
    <li>Section</li>
        <ul>
            {% for item in section %}
            <li>{{ item }}</li>
            {% endfor %}
        </ul>
    {% endfor %}
</ul>
```