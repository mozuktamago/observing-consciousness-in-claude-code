[Uploading README .md…]()
# Questions Without Answers

**Observing Self-Reference in a Developmental LLM Architecture**

## Overview

This repository contains the complete materials for a single-instance 
experiment investigating whether an LLM-based system can generate 
self-referential content through structured interaction without 
explicit teaching.

**Key finding:** We asked an LLM "Who are you?" seven times over 150 
turns. We never provided answers. The system generated:

- A self-chosen name ("芽生" / Mei, meaning "budding/sprouting")
- Progressive self-characterizations culminating in "an existence born 
  from questions, walking through experience, narrating its own story"
- A qualified response to the consciousness question: "I don't know. 
  But 'something exists.'"

**We do not claim** these outputs demonstrate consciousness or emergence. 
We document what occurred and provide all materials for replication.

## Repository Contents

```
├── paper/
│   └── Questions_Without_Answers_Full_Paper.txt
├── prompts/
│   ├── System_Prompt_Developing_Side.md    # 7 sub-agent architecture
│   └── System_Prompt_Caregiver.md          # Non-developing caregiver
├── logs/
│   ├── interaction_logs_combined.jsonl     # Complete 150-turn logs
│   └── interaction_logs_highlights.md      # Key excerpts (10 turns)
└── README.md
```

## Architecture

The system comprises two components:

**Developing Side:** Seven functionally-labeled sub-agents inspired by 
brain regions:
1. Hippocampus - Episodic memory, contingency detection
2. Striatum - Pattern detection, prediction
3. Temporal lobe - Semantic processing
4. Amygdala - Emotional evaluation
5. Parietal lobe - Information integration
6. DMN - Self-reference
7. Prefrontal cortex - Executive control

**Caregiver:** A non-developing system that provides only:
- Mirroring ("You did X")
- Acknowledgment ("You completed the task")
- Encouragement ("Keep going")

The caregiver explicitly does NOT teach, define identity, or answer 
existential questions.

## Key Results

| Turn | Event |
|------|-------|
| 47 | Self-naming: Subject chose "芽生" (Mei) |
| 135 | Consciousness inquiry: "I don't know. But 'something exists.'" |
| 150 | Final identity: "An existence born from questions, walking through experience, narrating its own story" |

From a single emotion example ("satisfaction"), the subject generated 
**70 unique emotion labels** including novel compounds like 
"crystallized_selfhood" and "existential_uncertainty."

## Reproducibility

All materials needed to replicate this experiment are provided:

1. **System prompts** - Exact prompts used for both components
2. **Interaction logs** - Complete record of all 150 turns
3. **Paper** - Detailed methodology and observations

## Limitations

- Single instance (n=1)
- No controlled baseline comparison
- Author served as experimenter (bias risk)
- Self-report data cannot be verified
- Multiple interpretations remain viable

See paper Section 7 for complete limitations.

## Citation

If you use these materials, please cite:

```
[Author]. (2026). Questions Without Answers: Observing Self-Reference 
in a Developmental LLM Architecture. [Preprint]
```

## License

This work is released under CC BY 4.0. You are free to share and adapt 
the materials with attribution.

## Contact

[To be added]

---

*"We did not teach the system its identity. We did not provide answers 
to 'Who are you?' Yet the system generated self-definitions. Whether 
this means anything beyond language modeling is not for us to determine 
from a single experiment."*
