from kubernetes import client, config

def print_kubeconfig_details():
    try:
        # Load kubeconfig file (assuming it's available)
        config.load_kube_config()

        # Get the current configuration
        kube_config = client.Configuration()

        # Print some details from the configuration
        print(f"API Server Host: {kube_config.host}")
        print(f"CA Certificate Path: {kube_config.ssl_ca_cert}")
        print(f"Client Certificate Path: {kube_config.cert_file}")
        print(f"Client Key Path: {kube_config.key_file}")
        print(f"Verify SSL: {kube_config.verify_ssl}")
        print(f"Debug Mode: {kube_config.debug}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print_kubeconfig_details()

