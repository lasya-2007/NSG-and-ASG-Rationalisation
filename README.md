# Azure NSG and ASG Rule Rationalisation

## Project Overview

This project focuses on simplifying Azure Network Security Group (NSG) rules by identifying IP-based rules that can potentially be rationalised using Application Security Groups (ASGs).

The goal is to reduce rule complexity and make network security policies easier to understand and maintain.

## Problem Statement

As applications grow, NSG configurations can contain multiple IP-based rules, duplicate rules, and conflicting rules.

Managing these rules manually can become difficult and error-prone.

Our solution analyzes NSG rules and identifies opportunities for rationalisation using ASG-based communication.

## Architecture

The prototype contains:

- Azure Virtual Network
- Web Subnet
- Application Subnet
- Web VM
- Application VM
- asg-web
- asg-app
- Network Security Group
- Python Rule Analyzer

