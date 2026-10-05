Local AI-Powered Security Log & Reconnaissance Analyzer
An automated, privacy-focused Security Operations Center (SOC) analysis pipeline that ingests active network telemetry (Nmap) and system event logs, processing them through a locally hosted Large Language Model (Llama 3.2 via Ollama) to generate structured, actionable threat intelligence reports.

Architecture & Workflow
Reconnaissance & Collection: Active host/network enumeration conducted via Kali Linux using Nmap service versioning (-sV) and NSE default scripts (-sC).

Local AI Pipeline: Python-based parser feeds raw execution logs and telemetry directly to a local Ollama instance running llama3.2.

Structured Reporting: Automatically evaluates exposed attack vectors, flags misconfigurations (e.g., SMB signing, unencrypted/self-signed administrative ports), and generates an executive summary with technical mitigation strategies in formatted Markdown (security_analysis_report.md).

Technical Stack
Environment: Windows 11 (Host) / Kali Linux (VM - NAT Network Mode)

LLM Engine: Ollama (llama3.2)

Orchestration: Python 3.12 (ollama library, pathlib)

Telemetry Source: Nmap network service enumeration & Sysmon/Auth logs

Discovered Vulnerabilities & Exposure Analysis
During simulated internal network reconnaissance against host interfaces, the analyzer successfully flagged key security exposures:

Ports 135/139/445 (RPC & SMB): Identified active SMB services with SMB2/3 message signing enabled but not required, leaving room for potential NTLM relay attempts.

Ports 8000/8089 (Splunk Web & Management): Identified active Splunk instances using default self-signed TLS certificates and exposed administrative login panels.

Setup & Execution
Prerequisites
Install Ollama and pull the Llama 3.2 model:

Bash
ollama pull llama3.2
Install Python dependencies:

Bash
pip install ollama
Running the Analyzer
Execute the Python script from your project folder:

PowerShell
python log_analyzer.py
Enter the path to your log or telemetry file when prompted (nmap_results.log or sample.log).

View the generated report in the terminal or open security_analysis_report.md.

Key Advantages
Zero External Data Leakage: All log processing happens 100% on-device—no cloud APIs or external LLM vendors required.

Standardized SOC Deliverables: Standardizes unstructured terminal outputs into clean executive summaries and prioritized remediation tasks.