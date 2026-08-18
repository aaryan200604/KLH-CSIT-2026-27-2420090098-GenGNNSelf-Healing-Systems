# Context-Aware Self-Healing Distributed Systems Using Generative Graph Neural Networks for Dynamic Fault Remediation

Modern distributed architectures face rapid cascading failures that static rule-based monitoring cannot efficiently isolate. This project introduces an autonomous self-healing framework driven by Generative Graph Neural Networks (GNNs) integrated into a MAPE-K control loop. Telemetry and service dependencies are modelled as dynamic spatio-temporal graphs. A Generative Graph Autoencoder detects structural anomalies, reconstructs baseline topologies, and synthesizes context-aware remediation workflows-including automated traffic rerouting and dynamic node isolation. Evaluated under synthetic chaos benchmarks, the system significantly reduces Mean Time to Remediation (MTTR) and prevents cascading system downtime.

## Team Members

| Roll No.    | Name       |
| :---------- | :--------- |
| 2420030669  | CH.ADITYA  |
| 2420030716  | K.GOKUL    |
| 2420090098  | A.AARYAN   |
| 2420030679  | G.Nishanth |

**Supervisor:** G.LAVANYA

## Architecture Breakdown

- Monitor: Telemetry listener continuously gathers metrics from distributed nodes and converts state to a graph representation.
- Analyze: Generative Graph Neural Network predicts node failure probabilities based on the network topology.
- Plan: Orchestrator takes the predicted probabilities and generates remediation plans.
- Execute: The orchestrator applies corrective actions such as node restart or traffic rerouting.
- Knowledge: Historical metrics and past action outcomes are retained for training and optimizing future iterations.

## Phase Deliverable Checklist

- [ ] review-1
- [ ] review-2
- [ ] review-3
- [ ] final

## Setup Instructions

1. Clone the repository
2. Run `./setup.ps1` to initialize the directory structure
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `.\venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
5. Install dependencies: `pip install -r requirements.txt`

## Execution

Execute the chaos runner:
`python src/fault_injection/chaos_runner.py`

Start the telemetry monitor:
`python src/monitor_analyze/telemetry_listener.py`
