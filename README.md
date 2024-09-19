# SSH Honeypot

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Planned Features for Future Releases](#planned-features-for-future-releases)
- [Important Notes](#important-notes)
- [Contributors](#contributors)

## Overview
This project implements a basic **SSH honeypot** using Python. A honeypot is a cybersecurity tool designed to detect, deflect, or counteract unauthorized attempts to access information systems. In the context of SSH, a honeypot can attract and monitor malicious actors attempting to gain unauthorized access to a system, offering valuable insights into attack patterns and methods.

## Prerequisites
- **Python 3.x**
- **Paramiko library**: Install via `pip install paramiko`

## Planned Features for Future Releases
- **Simulated File System**: Introduce a fake directory structure to further deceive attackers.
- **Interactive Web Interface**: Provide a user-friendly web-based dashboard for real-time monitoring.
- **Alerting Mechanism**: Implement email or SMS alerts when suspicious activities are detected.

## Important Notes
- This project is part of an academic exploration of cybersecurity concepts and is designed for educational purposes.
- **Security Warning**: When deploying the SSH honeypot, ensure it is isolated from sensitive systems. Proper network security measures should be in place to avoid unwanted exposure.
- This SSH honeypot is strictly for educational purposes and must not be used for unethical or malicious activities.
- **RSA Key Rotation**: The RSA key is regenerated every time the honeypot runs. Be sure to manually clear the `~/.ssh/known_hosts` file before each session to avoid conflicts.

## Contributors
- **Divyanshu Chaudhary**
