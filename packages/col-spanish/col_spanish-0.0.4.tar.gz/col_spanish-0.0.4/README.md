# col-spanish
A collection of tools to work with text write in Spanish (Colombia)


### Purpose of the Package
The purpose of the package is to create a group of functions that help to work with text in spanish, to be more accurate with spanish from Colombia.

### Features
+ normalization functions:
    - delete punctuation marks
    - delete accents

+ encrypting functions:
    - set_characters: 
        > delete duplicate characters inside the sentence. save it in the same order, 
        > as it appears in the sentence not in an aleatory order as set()
    - create_dictionary: 
        > Recieves two lists and create a dictionary where one is the key and the
        > other one is the value.
    - generate_pass: 
        > This function create a safe encrypted version of your data.

### Geting Started
The package can be found in Pypi, hence you can install it using pip
```bash
pip install col_spanish
```

### Usage
Using the normalization function to remove punctuation marks
```python
>>> from col_spanish import del_punctuation
>>> del_punctuation('Hola, ¿cómo estas? ¡bien!')
>>>
```

### Examples
```python
>>> from col_spanish import del_punctuation

>>> del_punctuation('Hola, ¿cómo estas? ¡bien!')
Hola cómo estas bien

>>> text = "Hola, ¿cómo estas? ¡bien!"
>>> normalized_text = del_punctuation(text)
>>> normalized_text
Hola cómo estas bien
```

### Contribution
Contributions are welcolme.
If you notice a bug let us know, thanks!

### Author
+ Main maintainer: Sergio A. Sosa Bautista (@sergioasb8)