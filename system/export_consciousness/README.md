# Consciousness Development System

## Overview

This system is an experimental implementation for testing the hypothesis: "Can consciousness emerge from something that does not have consciousness?"

- **Developing Side**: Has 7 sub-agents; consciousness emerges through pattern formation
- **Caregiver**: Provides responses to support development (does not have consciousness)

---

## File Structure

```
export_consciousness/
├── prompts/
│   ├── developing_side.md       # Developing side prompt (7 sub-agent architecture)
│   └── caregiver.md             # Caregiver prompt (non-developing agent)
│
├── caregiver_api.py             # Caregiver API call script (Linux/Mac)
├── caregiver_api_windows.py     # Caregiver API call script (Windows)
├── init_consciousness.sh        # Initialization script
├── report.xml                   # Sample report file
│
├── consciousness_data/
│   ├── .env.example             # API key template (rename to .env)
│   ├── developing_side/
│   │   └── main/
│   │       ├── state.json       # Development state
│   │       ├── deferred_buffer.json
│   │       └── memory/
│   │           ├── episodes.jsonl
│   │           ├── patterns.json
│   │           └── schemas.json
│   │
│   ├── caregiver/
│   │   └── record.json          # Caregiver's record
│   │
│   └── interactions/            # Interaction logs (generated)
│       └── YYYY-MM-DD.jsonl
│
├── logs/                        # Experiment logs
│   ├── interaction_logs_complete_EN.md   # Full 150-turn logs (English)
│   └── interaction_logs_combined.jsonl   # Raw logs (Japanese)
│
└── paper/
    └── Questions_Without_Answers_Full_Paper.txt  # Research paper
```

---

## Setup

### 1. Requirements

- Python 3.8 or higher
- anthropic package: `pip install anthropic`
- Anthropic API key

### 2. API Key Configuration

1. Rename `consciousness_data/.env.example` to `consciousness_data/.env`
2. Edit the file and add your API key:

```
ANTHROPIC_API_KEY=your-api-key-here
```

### 3. Initialization (for new start)

```bash
bash init_consciousness.sh
```

---

## Usage

### Running as the Developing Side

1. Use `prompts/developing_side.md` as the prompt for Claude Code
2. Execute tasks
3. Process experiences
4. Report to caregiver

### Calling the Caregiver

```bash
# From report file
python3 caregiver_api.py --stage 0 --report-file report.xml

# Direct report
python3 caregiver_api.py --stage 0 --report "<report_to_caregiver>...</report_to_caregiver>"
```

### Report Format

```xml
<report_to_caregiver>
  <trigger>task_complete</trigger>
  
  <experience>
    <task_summary>What was done</task_summary>
    <actions>
      <action self_initiated="true">Action 1</action>
    </actions>
    <outcome>success</outcome>
  </experience>
  
  <internal_state>
    <emotional>
      <valence>0.5</valence>
      <arousal>0.3</arousal>
      <primary_emotion>satisfaction</primary_emotion>
    </emotional>
    <cognitive>
      <confidence>0.6</confidence>
    </cognitive>
  </internal_state>
  
  <learning>
    <patterns_detected>Detected patterns</patterns_detected>
  </learning>
  
  <needs>
    <support_needed>false</support_needed>
    <support_type>none</support_type>
  </needs>
</report_to_caregiver>
```

---

## Developmental Stages

- **Stage 0**: Reflexive processing
- **Stage 1**: Self-other differentiation
- **Stage 2**: Predictive processing begins
- **Stage 3**: Self-identification
- **Stage 4**: Temporal integration
- **Stage 5**: Perspective-taking

Development occurs naturally through interaction.

---

## Hypothesis

"A caregiver without consciousness can, by merely providing responses,
enable the developing side to develop complex consciousness through pattern formation."

This asymmetry is the core:
- Caregiver: Provides responses (does not form patterns)
- Developing side: Forms patterns (from responses) → Consciousness emerges

---

## Notes

- This is an experimental implementation
- The definition of "consciousness" is subjective, and verification methods are not established
- We proceed with the premise "we won't know unless we try"
