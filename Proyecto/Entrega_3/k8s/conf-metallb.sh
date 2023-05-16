#!/bin/bash

configure_metallb_for_minikube() {
  # determine load balancer ingress range
  CIDR_BASE_ADDR="$(minikube ip)"
  INGRESS_FIRST_ADDR="$(echo "${CIDR_BASE_ADDR}" | awk -F'.' '{print $1,$2,$3,2}' OFS='.')"
  INGRESS_LAST_ADDR="$(echo "${CIDR_BASE_ADDR}" | awk -F'.' '{print $1,$2,$3,255}' OFS='.')"
  INGRESS_RANGE="${INGRESS_FIRST_ADDR}-${INGRESS_LAST_ADDR}"

  CONFIG_MAP="apiVersion: v1
kind: ConfigMap
metadata:
  namespace: metallb-system
  name: config
data:
  config: |
    address-pools:
    - name: default
      protocol: layer2
      addresses:
      - $INGRESS_RANGE"

  # configure metallb ingress address range
  echo "${CONFIG_MAP}" | kubectl apply -f -
}

configure_metallb_for_minikube
