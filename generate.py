#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

def render(name: str):
    template = env.get_template(name)
    with open(name, "w") as fh:
        fh.write(template.render())

render("index.html")
render("about.html")
