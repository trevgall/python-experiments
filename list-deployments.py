from kubernetes import client, config

#def main():
try:
    config.load_kube_config()
except:
    # load_kube_config throws if there is no config, but does not document what it throws, so I can't rely on any particular type here
    config.load_incluster_config()

v1 = client.AppsV1Api()
ret = v1.list_deployment_for_all_namespaces()

print('\nCurrent deployments : \n')
#print(f'{ret}')
for deploy in ret.items:
    #d_namespace = deploy.metadata.namespace
    #d_name = deploy.metadata.name
    print(f'Namespace : {deploy.metadata.namespace:<30s} Deployment : {deploy.metadata.name}')