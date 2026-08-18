import random
import time
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChaosRunner:
    def __init__(self, target_nodes: List[int]):
        self.target_nodes = target_nodes

    def inject_latency(self, node_id: int, latency_ms: int) -> None:
        logging.warning(f"Injecting {latency_ms}ms latency to node {node_id}")
        time.sleep(latency_ms / 1000.0)

    def crash_node(self, node_id: int) -> None:
        logging.error(f"Crashing node {node_id}")

    def run_chaos_experiment(self, duration: int) -> None:
        end_time = time.time() + duration
        while time.time() < end_time:
            node_to_attack = random.choice(self.target_nodes)
            attack_type = random.choice(["latency", "crash"])
            if attack_type == "latency":
                self.inject_latency(node_to_attack, random.randint(100, 500))
            else:
                self.crash_node(node_to_attack)
            time.sleep(random.randint(2, 5))
        logging.info("Chaos experiment completed.")

if __name__ == '__main__':
    runner = ChaosRunner(target_nodes=list(range(20)))
    runner.run_chaos_experiment(duration=30)
