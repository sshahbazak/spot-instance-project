from kubernetes import client, config, watch
import yaml

class CustomController:
    def __init__(self):
        config.load_kube_config()  # Load kubeconfig for in-cluster configuration

    def watch_custom_resource(self):
        print("Controller is now listening for events related to Custom Resources...")
        crd_api = client.CustomObjectsApi()
        resource_version = ''
        while True:
            stream = watch.Watch().stream(crd_api.list_cluster_custom_object, group='example.com', version='v1', plural='spotinstances', resource_version=resource_version)
            for event in stream:
                resource = event['object']
                resource_version = resource['metadata']['resourceVersion']
                if event['type'] == 'ADDED' or event['type'] == 'MODIFIED':
                    self.sync_custom_resource(resource)

    def sync_custom_resource(self, resource):
        # Example: Deploy the resource using the YAML manifest
        with open('spotinstance-manifest.yaml', 'w') as yaml_file:
            yaml.dump(resource, yaml_file)
        # Apply the YAML manifest using kubectl or client-python

if __name__ == "__main__":
    controller = CustomController()
    controller.watch_custom_resource()
