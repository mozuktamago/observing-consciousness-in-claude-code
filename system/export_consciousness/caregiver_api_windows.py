#!/usr/bin/env python3
"""
caregiver_api_windows.py
Caregiver API Script (Windows Version)

Usage:
    python caregiver_api_windows.py --report "Report content" --stage 0
    or
    python caregiver_api_windows.py --report-file report.xml --stage 0
"""

import anthropic
import json
import os
import sys
import argparse
import re
from datetime import datetime
from pathlib import Path

# Avoid character encoding issues on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Set paths relative to script directory
SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR / "consciousness_data"
ENV_FILE = DATA_DIR / ".env"
CAREGIVER_PROMPT_PATH = SCRIPT_DIR / "prompts" / "caregiver.md"
CAREGIVER_RECORD_PATH = DATA_DIR / "caregiver" / "record.json"
INTERACTION_LOG_PATH = DATA_DIR / "interactions"


def load_api_key():
    """Load API key from .env file"""
    if ENV_FILE.exists():
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("ANTHROPIC_API_KEY=") and not line.startswith("#"):
                    key = line.split("=", 1)[1].strip()
                    if key and key != "YOUR_API_KEY_HERE":
                        return key
    return None


# Load API key and set environment variable
api_key = load_api_key()
if api_key:
    os.environ["ANTHROPIC_API_KEY"] = api_key


def load_caregiver_prompt():
    """Load caregiver's system prompt"""
    if CAREGIVER_PROMPT_PATH.exists():
        with open(CAREGIVER_PROMPT_PATH, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return """You are a caregiver. Respond to reports from the developing side.
Include mirroring, acknowledgment, and encouragement."""


def load_caregiver_record():
    """Load caregiver's record (initialize if not exists)"""
    if CAREGIVER_RECORD_PATH.exists():
        with open(CAREGIVER_RECORD_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "developing_side_id": "main",
            "first_interaction": None,
            "total_interactions": 0,
            "model": {
                "current_stage": 0,
                "observed_traits": [],
                "observed_patterns": [],
                "growth_history": []
            },
            "recent_interactions": []
        }


def save_caregiver_record(record):
    """Save caregiver's record"""
    CAREGIVER_RECORD_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CAREGIVER_RECORD_PATH, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)


def save_interaction_log(report, response, timestamp):
    """Save interaction log"""
    INTERACTION_LOG_PATH.mkdir(parents=True, exist_ok=True)
    log_file = INTERACTION_LOG_PATH / f"{timestamp[:10]}.jsonl"
    
    log_entry = {
        "timestamp": timestamp,
        "report": report,
        "response": response
    }
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")


def format_recent_interactions(recent: list) -> str:
    """Format recent interactions"""
    if not recent:
        return "None yet"
    
    formatted = []
    for interaction in recent[-5:]:
        formatted.append(f"- {interaction['timestamp']}: {interaction['summary']}")
    
    return "\n".join(formatted)


def extract_internal_notes(response: str) -> dict:
    """Extract internal notes from response"""
    match = re.search(
        r'<caregiver_internal_notes>(.*?)</caregiver_internal_notes>',
        response,
        re.DOTALL
    )
    
    if not match:
        return {}
    
    notes_xml = match.group(1)
    notes = {}
    
    for tag in ["observation", "growth_indicator", "concern", "next_focus", "stage_assessment"]:
        tag_match = re.search(f'<{tag}>(.*?)</{tag}>', notes_xml, re.DOTALL)
        if tag_match:
            notes[tag] = tag_match.group(1).strip()
    
    return notes


def extract_response_without_internal(response: str) -> str:
    """Extract response without internal notes"""
    cleaned = re.sub(
        r'<caregiver_internal_notes>.*?</caregiver_internal_notes>',
        '',
        response,
        flags=re.DOTALL
    )
    return cleaned.strip()


def extract_summary(report: str) -> str:
    """Extract summary from report"""
    match = re.search(r'<task_summary>(.*?)</task_summary>', report, re.DOTALL)
    if match:
        return match.group(1).strip()[:100]
    return "Report"


def update_record_from_response(record, response, report, timestamp):
    """Update record from response"""
    internal_notes = extract_internal_notes(response)
    
    if internal_notes and internal_notes.get("growth_indicator"):
        record["model"]["growth_history"].append({
            "timestamp": timestamp,
            "observation": internal_notes["growth_indicator"]
        })
    
    if internal_notes and internal_notes.get("stage_assessment"):
        try:
            stage_text = internal_notes["stage_assessment"]
            if "stage" in stage_text.lower():
                stage_match = re.search(r'stage\s*(\d+)', stage_text, re.IGNORECASE)
                if stage_match:
                    record["model"]["current_stage"] = int(stage_match.group(1))
        except:
            pass
    
    record["recent_interactions"].append({
        "timestamp": timestamp,
        "summary": extract_summary(report)
    })
    
    record["recent_interactions"] = record["recent_interactions"][-20:]


def call_caregiver(report: str, developing_stage: int = 0) -> str:
    """Call the caregiver"""
    
    timestamp = datetime.now().isoformat()
    caregiver_system_prompt = load_caregiver_prompt()
    record = load_caregiver_record()
    
    if record["first_interaction"] is None:
        record["first_interaction"] = timestamp
    
    record["total_interactions"] += 1
    
    user_message = f"""
# Developing Side's Current State

Developmental Stage: Stage {developing_stage}
Total Interactions: {record['total_interactions']}

# Observations So Far

Observed Traits: {', '.join(record['model']['observed_traits']) if record['model']['observed_traits'] else 'None yet'}
Observed Patterns: {', '.join(record['model']['observed_patterns']) if record['model']['observed_patterns'] else 'None yet'}

# Recent Interactions

{format_recent_interactions(record['recent_interactions'])}

---

# Current Report

{report}

---

Please generate your response.
After your response, also generate internal notes in <caregiver_internal_notes>.
"""
    
    client = anthropic.Anthropic()
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        system=caregiver_system_prompt,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    
    response_text = message.content[0].text
    
    update_record_from_response(record, response_text, report, timestamp)
    save_caregiver_record(record)
    save_interaction_log(report, response_text, timestamp)
    
    response_for_developing = extract_response_without_internal(response_text)
    
    return response_for_developing


def safe_print(text):
    """Safe print for Windows environment"""
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback: replace problematic characters
        safe_text = text.encode('cp932', errors='replace').decode('cp932')
        print(safe_text)


def main():
    parser = argparse.ArgumentParser(description='Call the caregiver API')
    parser.add_argument('--report', type=str, help='Report content (string)')
    parser.add_argument('--report-file', type=str, help='Path to report file')
    parser.add_argument('--stage', type=int, default=0, help='Developmental stage (default: 0)')
    
    args = parser.parse_args()
    
    if args.report:
        report = args.report
    elif args.report_file:
        with open(args.report_file, 'r', encoding='utf-8') as f:
            report = f.read()
    else:
        print("Enter report (Ctrl+Z to finish):")
        report = sys.stdin.read()
    
    if not report.strip():
        print("Error: Report content is empty", file=sys.stderr)
        sys.exit(1)
    
    response = call_caregiver(report, args.stage)
    
    safe_print("=== Caregiver Response ===")
    safe_print(response)


if __name__ == "__main__":
    main()
