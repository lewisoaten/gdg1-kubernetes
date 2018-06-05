# gdg1-kubernetes
Demo repo for the GDG presentation

To have a play:
1. `minikube start`
2. `helm init`
3. `skaffold dev`
4. Now change `gdg-web/server.py` and observe that changes are built and deployed automatically
5. Uncomment hostname line and increase replicas in `gdg-web/helm/values.yaml` to see hello from different hosts
6. Uncomment memcached line and `gdg-web/helm/requirements.yaml` to see that data can be persisted outside of pods to safely load balance between them.
