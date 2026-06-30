#!/bin/bash
set -e

TAG=$1

echo "===== Updating Repository ====="
git fetch origin
git reset --hard origin/main

echo "===== Getting GKE Credentials ====="
gcloud container clusters get-credentials private-gke \
    --zone asia-south1-a \
    --project nisarga-499904

echo "===== Applying Kubernetes Manifests ====="
kubectl apply -f k8s/

echo "===== Updating Image ====="
kubectl set image deployment/gke-demo \
gke-demo=asia-south1-docker.pkg.dev/nisarga-499904/gke-demo/gke-demo:$TAG

echo "===== Waiting for Rollout ====="
kubectl rollout status deployment/gke-demo

echo "===== Deployment Successful ====="
