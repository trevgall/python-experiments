from kubernetes import client, config

def list_ingresses():
    try:
        # Load kubeconfig file (assuming it's available)
        config.load_kube_config()

        # Create Kubernetes API client
        api_instance = client.NetworkingV1Api()

        # List ingresses in the cluster
        ingresses = api_instance.list_ingress_for_all_namespaces()

        print("List of Ingresses:")
        for ingress in ingresses.items:
            print(f"Namespace: {ingress.metadata.namespace}, Name: {ingress.metadata.name}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_ingresses()
