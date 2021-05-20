import jinja2


def test_me() -> str:
    env = jinja2.Environment(
        loader=jinja2.PackageLoader("jinja_loader_bug"),
        autoescape=jinja2.select_autoescape(),
    )
    word = "hi"
    template = env.get_template("test_template.jinja")
    return template.render(word=word)
