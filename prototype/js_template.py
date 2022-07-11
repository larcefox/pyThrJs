# -*- coding: utf-8 -*-
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


class TemplateRender():
    def __call__(self, file, title, body):
        self.env = Environment()
        self.env.loader = FileSystemLoader('templates')
        template = self.env.get_template(file)
        template = self.render(template, title, body)
        template = self.encode_text(template)
        return template

    def encode_text(self, template):
        return template.encode(encoding='utf8')

    def render(self, template, title, body):
        return template.render(title=title, body=body)
