from kubernetes import client, config

def get_ingress_details():
    try:
        # Load kubeconfig file (assuming it's available)
        config.load_kube_config()

        # Create Kubernetes API client
        api_instance = client.NetworkingV1Api()

        # List ingresses in the cluster
        ingresses = api_instance.list_ingress_for_all_namespaces().items

        print("\nIngress Details:\n")

        for ingress in ingresses:  

            print(f"Namespace: {ingress.metadata.namespace:>25}")
            print(f"Name: {ingress.metadata.name:>30}\n")

            # Get ingress rules
            for rule in ingress.spec.rules:
                #print(f"  Host: {rule.host}")
                i_host = rule.host

                # Get ingress paths and backends
                for path in rule.http.paths:
                    #backend = path.backend
                    i_path = path.path
                    i_backend_service_name = path.backend.service.name
                    i_backend_service_port = path.backend.service.port.number
                    #print(f"    Path: {path.path}, Service Name: {backend.service.name}, Service Port: {backend.service.port}")
                    header = ('Host', 'Path', 'Service Name', 'Service Port')
                    print('%25s %25s %25s %25s' % header)                           # Print the headers out with formatting 
                    print(('-' * 25 + ' ') * len(header))                           # Print out a separator line   
                    print(f'{i_host:>25} {i_path:>25} {i_backend_service_name:>25} {i_backend_service_port:>25}\n')

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_ingress_details()

