def relative_from_root(path: str):
    import respublica_ui_tests
    from pathlib import Path

    return Path(respublica_ui_tests.__file__).parent.parent.joinpath(path).absolute().__str__()
