# Spot Instance Project
This is a repository for our cross-cloud spot instance project

Currently its divided into two sections - 

## Google Colab Notebook 
This folder contains all our analytical notebooks for our reliability model. They should also work loacally via jupyter notebook. 


## Kubernetes Controller Project 
This folder contains the logic to run our kubernetes cluster. Kubernetes has something called as CRD (Custom Resource Definition) which work hand in hand with a custom controller. This controller has the logic that decides which custom resources to deploy.


It is structured as follows - 
*    kubernetes - 
        *    crds - This folder contains CRDs utilized by our controller for configuring our custom resources, these typically dont change.

        *    manifests - This folder contains the base manifest. i.e. the starting infrastructure that could be deployed. 

* src - 
    *    tests - This folder contains the test manifests that I used in order to deploy additional spot instances.

    *    controller.py - This is the main controller logic. For now, the workflow works as follows - 
        you have kubectl apply <yaml file> command which talks with the Kubernetes API to send a new desired state (yaml file). 
        Our controller watches for changes in our custom resource. If detected it can make a decision if it wants to update our manifest.
        Kubernetes monitors the change in manifest and deploys whatever is needed based on configurations provided by our controller. 


## Steps to run this code locally - 

1. Install Docker Desktop. Enable Kubernetes via options in settings.
2. Open command prompt and type 'kubectl cluster-info' to verfiy kubernetes deployment. If not deployed try resetting the cluster. 
3. In one command prompt tab run the controller.py to continuously listen to changes in our custom resource. 
4. In another tab use 'kubectl apply <yaml file name>'. Use any yaml file in the test folder and view the change in the cluster configuration via 'kubectl get pods'.
