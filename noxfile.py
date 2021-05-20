from nox_poetry import Session
from nox_poetry import session


@session(python="3.9")
def tests(session: Session) -> None:
    session.install(".")
    session.install("pytest")
    session.run("pytest")
