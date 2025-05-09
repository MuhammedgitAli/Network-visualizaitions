# Real-Time Data Pipeline Prototype

This prototype demonstrates real-time data pipeline design and trade-offs in a hybrid cloud environment. It includes components for CDC simulation, stream transport, edge vs. cloud processing, and performance visualization.

## Components

### 1. CDC Simulation (`cdc_simulation.py`)
- Simulates database change events
- Generates JSON events every 100ms
- Demonstrates real-time data capture patterns

### 2. Kafka Pub/Sub (`kafka_pubsub.js`)
- Implements message publishing and consumption
- Uses KafkaJS for stream transport
- Demonstrates event-driven architecture

### 3. Edge vs. Cloud Processing
- `edge_server.js`: Simulates edge computing (10ms delay)
- `cloud_server.js`: Simulates cloud computing (100ms delay)
- Both expose identical endpoints for comparison

### 4. Performance Visualization (`visualize_performance.py`)
- Generates throughput vs. latency plots
- Creates network topology diagrams
- Helps visualize performance trade-offs

## Setup and Running

### 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-directory>
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Node.js dependencies
```bash
npm install
```

### 4. Start Kafka
- Download and extract Kafka from https://kafka.apache.org/downloads
- Start Zookeeper (if required) and Kafka server:
  ```bash
  # In one terminal
  bin/zookeeper-server-start.sh config/zookeeper.properties
  # In another terminal
  bin/kafka-server-start.sh config/server.properties
  ```
- By default, the code expects Kafka at `localhost:9092`. If your Kafka runs elsewhere, update the `brokers` array in `kafka_pubsub.js`.

### 5. Run the components

CDC Simulation:
```bash
python cdc_simulation.py
```

Kafka Pub/Sub:
```bash
npm run start:kafka
```

Edge Server:
```bash
npm run start:edge
```

Cloud Server:
```bash
npm run start:cloud
```

Generate Visualizations:
```bash
python visualize_performance.py
```

- The performance plot will pop up automatically.
- The network diagram will open in your default browser.

## Architecture Insights

1. **Latency Trade-offs**
   - Edge processing offers lower latency (10ms)
   - Cloud processing provides more resources but higher latency (100ms)
   - The visualization shows the inverse relationship between throughput and latency

2. **Reliability**
   - Kafka provides reliable message delivery
   - Edge servers can handle local requests even during cloud outages
   - Hybrid architecture improves overall system resilience

3. **Scalability**
   - Edge servers can handle local traffic independently
   - Cloud servers provide centralized processing for complex tasks
   - The system can scale horizontally at both edge and cloud levels

## Network Topology

The system demonstrates two network topologies:
1. Flat CDN: Traditional content delivery network
2. Hybrid P2P/CDN: Peer-to-peer enhanced content delivery

The visualization shows how the hybrid approach can reduce latency and improve scalability through peer-to-peer connections while maintaining the reliability of CDN infrastructure.

---

## Notes for Forking and Running
- This project is cross-platform (Windows, macOS, Linux).
- All dependencies are standard and listed in `requirements.txt` and `package.json`.
- Make sure Kafka is running and accessible at the address specified in `kafka_pubsub.js`.
- If you use a virtual environment for Python, activate it before installing dependencies.
- If you encounter port conflicts, you can change the ports in the server scripts. 