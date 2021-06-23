import jmespath
import yaml


def without_jmespath():
    with open("deployment.yaml") as deploy_yaml:
        deployment = yaml.safe_load(deploy_yaml)

    containers = deployment["spec"]["template"]["spec"]["containers"]

    # We could get away with using containers[0] here, but it will break if we ever add a sidecar container, and we
    # have to use a generator for the env section anyway, so let's not cheat here either.
    nginx_container = next(c for c in containers if c["name"] == "nginx")
    nginx_port_env = next(e for e in nginx_container["env"] if e["name"] == "NGINX_PORT")
    nginx_port_env["value"] = 8080

    return deployment


def with_jmespath():
    with open("deployment.yaml") as deploy_yaml:
        deployment = yaml.safe_load(deploy_yaml)

    nginx_port_env = jmespath.search(
        "spec.template.spec.containers[?name=='nginx']|[0].env[?name=='NGINX_PORT']|[0]",
        deployment,
    )
    nginx_port_env["value"] = 8080

    return deployment
