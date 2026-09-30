![HTML-CSS-JS CODE](https://github.com/memphis-tools/crook-ops/actions/workflows/verify.yml/badge.svg?branch=main)
![TOMCAT ON STANDALONE](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/memphis-tools/crook-ops/main/.status/site1.json)
![TOMCAT ON CONTAINER](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/memphis-tools/crook-ops/main/.status/site2.json)
![TOMCAT ON PODS](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/memphis-tools/crook-ops/main/.status/site3.json)
![Screenshot](pictures/illustration.png)

# Crook Ops

A small AWS deployment project serving the same application through three different environments.

**Domain:** `crook-ops.dev` (registered with [Namecheap](https://www.namecheap.com/))

The kubernetes cluster is only run on demand.

## Services

| Environment            | URL                                         |
| ---------------------- | ------------------------------------------- |
| Tomcat on EC2          | https://app.crook-ops.dev/crook-ops/        |
| Docker / Tomcat on EC2 | https://app.crook-ops.dev/docker/crook-ops/ |
| Kubernetes / EKS       | https://app.crook-ops.dev/k8s/crook-ops/    |

## Architecture

```text
                       CROOK OPS
                          │
                  ┌───────┴───────┐
                  |    GitHub     │
                  │  crook-ops    │
                  └───────┬───────┘                   
         ┌────────────────┴────────────────┐
         │                                 │
         ▼                                 ▼
    ─────────────┐                 ┌───────────────┐
   |    AWS      │                 │  DIGITALOCEAN │
    ─────┬───────┘                 └───────┬───────┘
         │                                 │
         ▼                                 ▼
 ┌───────────────┐                 ┌───────────────┐
 │  HTTPS :443   │                 │  Static Site  │
 │   AWS ALB     │                 │    public/    │
 └───────┬───────┘                 └───────┬───────┘
         │                                 │
 ┌───────┼────────┐                        ▼
 │       │        │                ┌───────────────┐
 ▼       ▼        ▼                │   HTML / CSS  │
 Tomcat   Docker  EKS              │      / JS     │
 EC2     Tomcat                    └───────────────┘
 EC2     ▼
 Pods
```
