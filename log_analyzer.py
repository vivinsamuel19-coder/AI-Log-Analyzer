import sys
import ollama

def analyze_security_log(file_path):
    """Reads a log file and uses local Llama 3.2 to generate a security report."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            log_data = f.read()
    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' not found.")
        return None

    print(f"[+] Processing '{file_path}' with Llama 3.2...")

    system_prompt = """
    You are a Lead SOC Analyst. Analyze the provided security event logs or scan telemetry.
    Generate a professional Markdown security report covering:
    1. Executive Summary: High-level overview of findings.
    2. Event Details & Discovered Services: Breakdown of notable entries or open ports.
    3. Threat & Vulnerability Assessment: Identify risks, anomalies, or potential exploits.
    4. Recommended Mitigation Steps: Actionable defensive hardening steps.
    """

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Log Telemetry Data:\n{log_data}"}
            ]
        )
        return response["message"]["content"]
    except Exception as e:
        print(f"[!] Ollama API Error: {e}")
        return None

def save_report(report_content, filename="security_analysis_report.md"):
    """Saves the generated AI analysis report to a Markdown file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"[+] Report saved to: {filename}")

if __name__ == "__main__":
    print("=" * 60)
    print("      AI-POWERED LOCAL LOG ANALYZER           ")
    print("=" * 60)

    log_file = input("Enter path to log file [e.g., sample.log]: ").strip()
    if not log_file:
        print("[!] No file path entered.")
        sys.exit(1)

    report = analyze_security_log(log_file)

    if report:
        print("\n" + "=" * 60)
        print("                  AI ANALYSIS OUTPUT                      ")
        print("=" * 60 + "\n")
        print(report)
        save_report(report)