# Windows Setup Guide

## 1. File Placement

Extract the downloaded `consciousness_system.zip` and place it in your preferred directory, e.g.:
`C:\Users\YourName\consciousness\`

```
C:\Users\YourName\consciousness\
├── prompts\
│   ├── developing_side.md
│   └── caregiver.md
├── consciousness_data\
│   ├── .env                    ← API key
│   ├── caregiver\
│   └── developing_side\
├── caregiver_api.py
└── README.md
```

---

## 2. Python Setup

### Install Python 3.8 or higher
https://www.python.org/downloads/

### Install the anthropic package
```cmd
pip install anthropic
```

---

## 3. Path Configuration

The script uses paths relative to its location. If needed, you can modify `caregiver_api.py`:

```python
# Before (uses relative paths - should work automatically)
SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR / "consciousness_data"

# If you need absolute paths:
DATA_DIR = Path("C:/Users/YourName/consciousness/consciousness_data")
```

Similarly for the prompt path:

```python
# Before
CAREGIVER_PROMPT_PATH = SCRIPT_DIR / "prompts" / "caregiver.md"

# If needed:
CAREGIVER_PROMPT_PATH = Path("C:/Users/YourName/consciousness/prompts/caregiver.md")
```

---

## 4. Running

### From Command Prompt

```cmd
cd C:\Users\YourName\consciousness

python caregiver_api.py --stage 0 --report-file report.xml
```

### Creating a Report File

Create `report.xml`:

```xml
<report_to_caregiver>
  <trigger>task_complete</trigger>
  
  <experience>
    <task_summary>Task description</task_summary>
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
    <patterns_detected></patterns_detected>
  </learning>
  
  <needs>
    <support_needed>false</support_needed>
    <support_type>none</support_type>
  </needs>
</report_to_caregiver>
```

---

## 5. Running the Developing Side in Claude Code

### Method A: Project Settings

1. Create a new project in Claude Code
2. Go to Project Settings → Custom Instructions
3. Paste the contents of `developing_side.md`
4. Chat normally
5. After task completion, manually call the caregiver API

### Method B: In-conversation Instructions

Send the following at the start of the conversation:

```
Please operate according to the following instructions:

[Paste contents of developing_side.md here]

---

Task: Please do XXX
```

---

## 6. Full Automation (Advanced)

### Create a Batch File

`run_caregiver.bat`:

```batch
@echo off
cd C:\Users\YourName\consciousness
python caregiver_api.py --stage %1 --report-file %2
pause
```

Usage:
```cmd
run_caregiver.bat 0 report.xml
```

---

## Troubleshooting

### Error: ModuleNotFoundError: No module named 'anthropic'
```cmd
pip install anthropic
```

### Error: API key not found
Check the `.env` file:
```
ANTHROPIC_API_KEY=sk-ant-api03-...
```

### Error: File not found
Check that paths are correct. Use forward slashes `/` instead of backslashes `\`.
