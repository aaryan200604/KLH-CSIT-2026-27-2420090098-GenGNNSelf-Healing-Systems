import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HealingOrchestrator:
    def __init__(self):
        self.remediation_history: List[Dict[str, Any]] = []

    def plan(self, predictions: List[int]) -> List[Dict[str, Any]]:
        actions = []
        for node_id, pred in enumerate(predictions):
            if pred == 1:
                actions.append({"node_id": node_id, "action": "restart"})
            elif pred == 2:
                actions.append({"node_id": node_id, "action": "reroute"})
        return actions

    def execute(self, actions: List[Dict[str, Any]]) -> None:
        for action in actions:
            node_id = action.get("node_id")
            action_type = action.get("action")
            logging.info(f"Executing {action_type} on node {node_id}")
            self.remediation_history.append(action)

    def process_cycle(self, predictions: List[int]) -> None:
        actions = self.plan(predictions)
        if actions:
            self.execute(actions)
        else:
            logging.info("No remediation actions required.")
