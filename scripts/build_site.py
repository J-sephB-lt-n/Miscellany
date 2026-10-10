"""
Build the files defining the site by populating all of the file templates.
"""

import jinja2

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader("./templates"))


def main() -> None:
    """
    Render the site.
    """
    index_template = template_env.get_template("index.html.j2")
    index_html: str = index_template.render()
    with open("index.html", "w") as file:
        file.write(index_html)


if __name__ == "__main__":
    main()
