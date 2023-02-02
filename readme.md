# Django-React Prototype Application

## Intoduction

This is a Django project combining the major features of both frameworks/libraries

## Setup

### Clone project

```
git clone ...
```

### Navigate into the Github project

```
cd Django-React
```

### Create a virtual environment

```
python -m .venv
```

### Activate the virtual environment

```
"./.venv/Scripts/activate" # Command Prompt
./.venv/Scripts/Activate.ps1 # PowerShell
```

### Install packages

```
pip install -r requirements.txt
```

### Navigate into the django project

```
cd django_react_roject
```

### Seed Database

```
python manage.py shell
```

(only example data)

```python
from django_react_app.models import Product

Product.objects.create(name="Football")
Product.objects.create(name="Book")
Product.objects.create(name="Keyboard")
Product.objects.create(name="Bike")
```

### Start Server

```
python manage.py runserver
```

The website is now available at localhost:8000

## Usage of React and Django

### Integration

Head of html file in temlates directory (products.html)

```html
<script
	src="https://unpkg.com/react@18/umd/react.development.js"
	crossorigin></script>
<script
	src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"
	crossorigin></script>
<script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
```

### Parsing context data to the template

When parsing data to react we need a Serializer

```python
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']
```

```python
def prductsView(request):
    snippets = Product.objects.all()
    serializer = ProductsSerializer(snippets, many=True)
    products = str(JSONRenderer().render(serializer.data), 'utf-8')

    context = {
        'django_products': Product.objects.all(),
        'react_products': products
    }

    return render(request, 'products.html', context=context)
```

### Template usage

#### Django option

we can use the standard Django template functions to render out the data

```html
<div class="django">
	<h2>Django approach</h2>
	<div>
		{% for item in django_products %}
		<p>Productname: <b>{{item.name}}</b></p>
		{% endfor %}
	</div>
</div>
```

#### React option

we need a root for the React application

```html
<div id="react_root"></div>
```

the react logic goes in the script tag

```js
<script type="text/babel"> // It is important to declare type="text/babel" to use jsx
    const domContainer = document.querySelector("#react_root")
    const root = ReactDOM.createRoot(domContainer)
    function ProductsList() { // usage of components
        let products = JSON.parse("{{react_products}}".replace(/&quot;/g, '"')) // Django parses the data in the curly braces to react. It is important take this data to the json format and replacing the quotes
        return (
            <div>
                {/* The way React renders out the data */}
                {/* Note arrow function didn't work */}
                {products.map(function (item) {
                    return (
                        <p key={item.id}>
                            Productname: <b>{item.name}</b>
                        </p>
                    )
                })}
            </div>
        )
    }
    function ReactApp() {
        return (
            <div>
                <h2>React approach</h2>
                <ProductsList />
            </div>
        )
    }

    root.render(<ReactApp />)
</script>
```
