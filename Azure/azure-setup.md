# Azure Setup

## Resource Group
- Name: rg-nsg-rationalisation
- Region: Central India

## Virtual Network
- Name: vnet-nsg-rationalisation
- Address Space: 10.0.0.0/16

## Subnets
- WebSubnet: 10.0.1.0/24
- AppSubnet: 10.0.2.0/24

## Virtual Machines
- Web VM: vm-web
- Web Private IP: 10.0.1.4
- App VM: vm-app
- App Private IP: 10.0.2.4

## Application Security Groups
- asg-web
- asg-app

## Network Security Group
- Name: nsg-rationalisation

## Custom NSG Rules

### IP-based rule
- Name: Allow-Web-To-App-8080
- Source: 10.0.1.0/24
- Destination: 10.0.2.0/24
- Protocol: TCP
- Port: 8080
- Action: Allow

### ASG-based rule
- Name: Allow-Web-ASG-To-App-8080
- Source: asg-web
- Destination: asg-app
- Protocol: TCP
- Port: 8080
- Action: Allow

## Rationalisation

The Python analyzer identifies the IP-based Web-to-App rule
as a candidate for ASG-based rationalisation.

Proposed change:

IP-based:
10.0.1.0/24 → 10.0.2.0/24

ASG-based:
asg-web → asg-app

The proposed configuration can reduce the custom rule count
from 2 to 1, which represents a proposed 50% reduction.m