#!/usr/bin/python3
from cmdroute import entrypoint, dispatch


@entrypoint()
def wow(name, greeting="Hello"):
    print(greeting + ", " + name)


@entrypoint()
def greetings(name, greeting="Hello"):
    """
    greetings is a greeter utility

    u can use it with different greeting parameters
    """
    print(greeting + ", " + name)


@entrypoint()
def arraytry(arra, greeting=[1]):
    """
    greetings is a greeter utility

    u can use it with different greeting parameters
    """
    print(str(arra) + ", " + str(greeting))


dispatch()
