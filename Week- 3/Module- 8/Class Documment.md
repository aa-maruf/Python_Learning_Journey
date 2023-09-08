
Source: https://docs.python.org/3/tutorial/classes.html 
Beginner-friendly notes on classes in Python:

- A **class** is a blueprint for creating objects. It defines the attributes and behaviors of the objects that will be created from it.
- To define a class in Python, you use the `class` keyword, followed by the name of the class and a colon. The body of the class is indented and contains the definitions of the attributes and methods of the class.
- An **attribute** is a variable that belongs to an object. It stores data about the object¹[1]. You can define attributes in the body of the class, or you can add them to an object after it has been created.
- A **method** is a function that belongs to an object²[2]. It defines an action that the object can perform. You define methods in the body of the class, just like you define functions outside of a class.
- To create an object from a class, you call the class as if it were a function. This creates a new instance of the class and returns it³[3]. You can then assign this instance to a variable to use it.
- Here's an example that shows how to define a simple `Dog` class with two attributes (`name` and `age`) and one method (`bark`):

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} barks!")
```

- In this example, we define a `Dog` class with an `__init__` method and a `bark` method.
- The `__init__` method is a special method that gets called when you create a new instance of the class. It's used to initialize the attributes of the object. In this case, we use it to set the `name` and `age` attributes of the `Dog` object.
- The `bark` method is a regular method that defines an action that a `Dog` object can perform. In this case, it prints out a message saying that the dog barks.
- Here's how you can create a new `Dog` object and use its methods:

```python
my_dog = Dog("Rufus", 3)
my_dog.bark()
```

- In this example, we create a new `Dog` object by calling the `Dog` class as if it were a function. We pass in two arguments: `"Rufus"` for the `name` attribute and `3` for the `age` attribute.
- We then assign this new `Dog` object to the variable `my_dog`.
- Finally, we call the `bark` method on the `my_dog` object by using dot notation (`my_dog.bark()`). This prints out the message `"Rufus barks!"`.
  
