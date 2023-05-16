#!/bin/bash

# Set chart name
CHART_NAME=tpm_chart

# Create directory structure
mkdir -p ${CHART_NAME}/templates

# Write content to files

echo "apiVersion: v2
name: ${CHART_NAME}
description: A Helm chart for the Text Processor Microservice
version: 1.0.0" > ${CHART_NAME}/Chart.yaml

echo "replicaCount: 1

image:
  repository: abhimazu/text-processor
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 5000

resources: {}" > ${CHART_NAME}/values.yaml

echo "apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include \"${CHART_NAME}.fullname\" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: {{ include \"${CHART_NAME}.fullname\" . }}
  template:
    metadata:
      labels:
        app: {{ include \"${CHART_NAME}.fullname\" . }}
    spec:
      containers:
        - name: {{ .Chart.Name }}
          image: \"{{ .Values.image.repository }}:{{ .Chart.AppVersion }}\"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: 5000
              protocol: TCP
          resources:
            {{- toYaml .Values.resources | nindent 12 }}" > ${CHART_NAME}/templates/deployment.yaml

echo "apiVersion: v1
kind: Service
metadata:
  name: {{ include \"${CHART_NAME}.fullname\" . }}
spec:
  type: {{ .Values.service.type }}
  ports:
    - port: {{ .Values.service.port }}
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app: {{ include \"${CHART_NAME}.fullname\" . }}" > ${CHART_NAME}/templates/service.yaml

echo "Helm chart has been created!"

