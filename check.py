from flask import *

app = Flask(__name__)


@app.route('/')
def entry_page():
    return render_template('shoppinglist.html')


@app.route('/showitems', methods=['POST'])
def show():
    item = request.form['item']
    id = request.form['id']
    price = request.form['price']
    quantity = request.form['quantity']
    return render_template('showitems.html', item=item, id=id, price=price, quantity=quantity)


if __name__ == '__main__':
    app.run(debug=True)
