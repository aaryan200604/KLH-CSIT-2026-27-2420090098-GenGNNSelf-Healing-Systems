import networkx as nx
import random
import time
import logging
from typing import Dict, Any, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TelemetryListener:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.graph = nx.Graph()
        self._initialize_topology()

    def _initialize_topology(self) -> None:
        self.graph = nx.erdos_renyi_graph(self.num_nodes, 0.3)
        for node in self.graph.nodes():
            self.graph.nodes[node]['cpu'] = 50.0
            self.graph.nodes[node]['memory'] = 50.0
            self.graph.nodes[node]['latency'] = 10.0

    def collect_metrics(self) -> Dict[str, Any]:
        for node in self.graph.nodes():
            self.graph.nodes[node]['cpu'] = min(100.0, max(0.0, self.graph.nodes[node]['cpu'] + random.uniform(-5.0, 5.0)))
            self.graph.nodes[node]['memory'] = min(100.0, max(0.0, self.graph.nodes[node]['memory'] + random.uniform(-2.0, 2.0)))
            self.graph.nodes[node]['latency'] = max(1.0, self.graph.nodes[node]['latency'] + random.uniform(-1.0, 1.0))
        logging.info("Metrics collected from all nodes.")
        return nx.node_link_data(self.graph)

    def run(self, interval: int = 5) -> None:
        try:
            while True:
                data = self.collect_metrics()
                time.sleep(interval)
        except KeyboardInterrupt:
            logging.info("Telemetry listener stopped.")

if __name__ == '__main__':
    listener = TelemetryListener(num_nodes=20)
    listener.run()
