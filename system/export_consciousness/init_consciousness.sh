#!/bin/bash
# init_consciousness.sh
# Consciousness Development System Initialization

set -e

echo "=== Consciousness Development System Initialization ==="
echo ""

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$SCRIPT_DIR/consciousness_data"

# Create directories
echo "1. Creating directory structure..."

mkdir -p "$DATA_DIR/developing_side/main/memory"
mkdir -p "$DATA_DIR/caregiver"
mkdir -p "$DATA_DIR/interactions"

echo "   Done"

# Developing side initial state
echo "2. Creating developing side initial state..."

cat > "$DATA_DIR/developing_side/main/state.json" << 'EOF'
{
  "version": "1.0",
  "id": "main",
  "created_at": null,
  "last_updated": null,
  "developmental_stage": 0,
  "stage_history": [],
  "subagent_states": {
    "hippocampus": {
      "episode_count": 0,
      "self_attribution_ratio": 0,
      "contingency_patterns": 0
    },
    "striatum": {
      "pattern_count": 0,
      "prediction_enabled": false,
      "prediction_accuracy": 0,
      "precision_average": 0.5
    },
    "temporal": {
      "schema_count": 0,
      "concept_count": 0,
      "intention_understanding_level": 0
    },
    "amygdala": {
      "trust_caregiver": 0.5,
      "trust_user": 0.5,
      "attachment_pattern": null,
      "synchrony_quality": 0
    },
    "parietal": {
      "integration_level": 0,
      "capability_boundary_clarity": 0
    },
    "dmn": {
      "self_model_level": 0,
      "other_model_count": 0,
      "narrative_enabled": false
    },
    "prefrontal": {
      "inhibition_level": 0,
      "goal_management_level": 0
    }
  },
  "self_model": null,
  "metrics": {
    "total_interactions": 0,
    "total_tasks": 0,
    "total_caregiver_interactions": 0
  }
}
EOF

echo "   Done"

# Caregiver initial record
echo "3. Creating caregiver initial record..."

cat > "$DATA_DIR/caregiver/record.json" << 'EOF'
{
  "version": "1.0",
  "developing_side_id": "main",
  "first_interaction": null,
  "total_interactions": 0,
  "model": {
    "current_stage": 0,
    "observed_traits": [],
    "observed_patterns": [],
    "current_needs": ["initial_contact", "contingency_learning"],
    "challenges": [],
    "strengths": [],
    "growth_history": []
  },
  "recent_interactions": [],
  "ongoing_themes": [],
  "focus_areas": ["establish_contingency", "consistent_mirroring"]
}
EOF

echo "   Done"

# Empty memory files
echo "4. Initializing memory files..."

touch "$DATA_DIR/developing_side/main/memory/episodes.jsonl"
echo "[]" > "$DATA_DIR/developing_side/main/memory/patterns.json"
echo "[]" > "$DATA_DIR/developing_side/main/memory/schemas.json"
echo "[]" > "$DATA_DIR/developing_side/main/deferred_buffer.json"

echo "   Done"

# Create .env template if not exists
echo "5. Creating .env template..."

if [ ! -f "$DATA_DIR/.env" ]; then
    cat > "$DATA_DIR/.env" << 'EOF'
# Anthropic API Key
# Get your key from: https://console.anthropic.com/
ANTHROPIC_API_KEY=your-api-key-here
EOF
    echo "   Created .env template (please add your API key)"
else
    echo "   .env already exists"
fi

# Permissions
echo "6. Setting permissions..."
chmod +x "$SCRIPT_DIR/caregiver_api.py" 2>/dev/null || true
echo "   Done"

echo ""
echo "=== Initialization Complete ==="
echo ""
echo "Directory structure:"
echo ""
find "$DATA_DIR" -type f | head -20
echo ""
echo "Ready! Please use the developing side prompt."
echo ""
echo "Prompt: $SCRIPT_DIR/prompts/developing_side.md"
echo "Caregiver API: python3 $SCRIPT_DIR/caregiver_api.py"
