import pathlib

import edit_deployment
import yaml

SCRIPT_DIR = pathlib.Path(__file__).parent.absolute()


def test_without_jmespath():
    # Load fixture
    with open(SCRIPT_DIR.joinpath("edited_deployment.yaml")) as yml:
        test_deployment = yaml.safe_load(yml)

    # Run function and compare results
    deployment = edit_deployment.without_jmespath()
    assert deployment == test_deployment


def test_with_jmespath():
    # Load fixture
    with open(SCRIPT_DIR.joinpath("edited_deployment.yaml")) as yml:
        test_deployment = yaml.safe_load(yml)

    # Run function and compare results
    deployment = edit_deployment.with_jmespath()
    assert deployment == test_deployment
