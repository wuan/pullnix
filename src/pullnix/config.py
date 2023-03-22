from dataclasses import dataclass


@dataclass
class Config:
    repos: dict


def load_config(config_path="/etc/pullnix.yml") -> Config:
    import yaml
    with open(config_path) as f:
        # use safe_load instead load
        return Config(**(yaml.safe_load(f)))
