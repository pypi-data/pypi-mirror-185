# IziToast

izitoast is an Elegant, responsive, flexible, and lightweight notification plugin with no dependencies.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install izitoast.



## Usage

Add 'izitoast' to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
     '...',
    'izitoast',
]
```

inside base template file at last position include a single line of code

```html
...
{% include 'includes/izitoast.html' %}
</body>
</html>
```

## Working
- User can pass option diversify or not, if not pass diversify option, izitoast will take default settings
- Single message with specified tag
```python
from izitoast.functions import izitoast

def func(request):
    ...
    message = "This is success message."
    diversify = {
        "position": "topRight",
        "transition_in": "flipInX",
        "transition_out": "flipOutX",
        "time_out": 3000,
    }

    izitoast(request=request, model="success", message=message, diversify=diversify)

    return render(request, 'template.html')
```
- Multiple messages with different tags at a time
```python
from izitoast.functions import izitoast

def func(request):
    ...
    message = {
        'raw': [
            {
                'tag': 'success',
                'item': "Success message"
            },
            {
                'tag': 'info',
                'item': "Information message!"
            },
            {
                'tag': 'warning',
                'item': "Warning message!"
            },
            {
                'tag': 'danger',
                'item': "Error message!"
            }
        ]
    }
    diversify = {
        "position": "topRight",
        "transition_in": "flipInX",
        "transition_out": "flipOutX",
        "time_out": 3000,
    }

    izitoast(request=request, model="success", message=message, diversify=diversify)

    return render(request, 'template.html')
```

## generate form.errors
```python
from izitoast.functions import izitoast

def func(request):
    ...
    
    diversify = {
        "position": "topRight",
        "transition_in": "flipInX",
        "transition_out": "flipOutX",
        "time_out": 3000,
    }
    izitoast(request=request, model="form-error", message=form.errors, diversify=diversify)

    return render(request, 'template.html')
```


## model

- Users can choose different models and it can be 'success', 'info', 'warning', or 'danger'. 

- but when generating form.errors must be set to 'model=form-error'.


## Optionals
1. position: 

 - Default izitoast shown place "topRight",

 - It can be: [bottomRight, bottomLeft, topRight, topLeft, topCenter, bottomCenter, center]

2. transition_in:

 - Default izitoast open animation "flipInX",

 - It can be: [bounceInLeft, bounceInRight, bounceInUp, bounceInDown, fadeIn, fadeInDown, fadeInUp, fadeInLeft, fadeInRight, flipInX]

3. transition_out:
 - Default izitoast close animation "flipOutX",

 - It can be: [fadeOut, fadeOutUp, fadeOutDown, fadeOutLeft, fadeOutRight, flipOutX]

4. time_out:
  - the default value is 3000.


## Dependencies

 - It uses [izitoast v1.4.0](https://izitoast.marcelodolza.com/) scripts and styles.

#### For message transferring uses messages 
```python 
from django.contrib import messages
```


## Demo

[Django-IziToast](https://djangoizitoast.pythonanywhere.com/)

## GitHub

[Django-IziToast](https://github.com/abdulrahim-uj/izitoast/)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)





