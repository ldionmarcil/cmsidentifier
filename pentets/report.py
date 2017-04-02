from jinja2 import Template

class Report():
    @classmethod
    def from_file(cls, layout_path, scan):
        with open(layout_path, 'r') as f:
            return cls(f.read(), scan)

    def __init__(self, layout, scan):
        self.layout = layout
        self.scan = scan

    def render(self):
        template = Template(self.layout)
        return template.render(scan = self.scan)

    def dump(self, io):
        output = self.render()
        io.write(output)
