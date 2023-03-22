import pullnix


def test_load(tmp_path):
    config_path = tmp_path / "config.yml"
    with open(config_path, "w") as file:
        file.write("""
        repos:
          base: git@github.com:foo/bar.git
        """)
    result = pullnix.config.load_config(config_path)
    print(result)
