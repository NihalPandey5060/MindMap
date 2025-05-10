from tinydb import TinyDB, Query
from datetime import datetime
from typing import Dict, List, Any

class InteractionLogger:
    def __init__(self, db_path: str = "interactions.json"):
        """Initialize the interaction logger with TinyDB."""
        self.db = TinyDB(db_path)
        self.interactions = self.db.table('interactions')
    
    def log_interaction(self, input_data: Dict[str, Any], prediction: Any) -> None:
        """Log a user interaction with timestamp."""
        interaction = {
            'timestamp': datetime.now().isoformat(),
            'input': input_data,
            'prediction': str(prediction)  # Convert prediction to string for storage
        }
        self.interactions.insert(interaction)
    
    def get_recent_interactions(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get the most recent interactions."""
        return self.interactions.all()[-limit:]
    
    def clear_history(self) -> None:
        """Clear all interaction history."""
        self.interactions.truncate()
    
    def get_interaction_count(self) -> int:
        """Get the total number of interactions logged."""
        return len(self.interactions) 