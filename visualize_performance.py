import matplotlib.pyplot as plt
import numpy as np
import webbrowser
import os

def plot_throughput_latency():
    # Generate sample data with more realistic throughput calculation
    latency = np.linspace(10, 1000, 100)  # ms
    
    # More realistic throughput calculation considering:
    # - Base throughput capacity
    # - Latency impact on throughput
    # - Diminishing returns at higher latencies
    base_throughput = 100  # Base requests per second
    throughput = base_throughput * np.exp(-latency/500)  # Exponential decay model
    
    plt.figure(figsize=(10, 6))
    plt.plot(latency, throughput, 'b-', label='Throughput vs Latency')
    plt.scatter([10, 100], [throughput[0], throughput[10]], color='red', label='Edge vs Cloud')
    
    plt.xlabel('Latency (ms)')
    plt.ylabel('Throughput (requests/second)')
    plt.title('Performance Trade-off: Throughput vs Latency')
    plt.grid(True)
    plt.legend()
    
    # Save the plot
    plt.savefig('performance_plot.png')
    # Show the plot
    plt.show()

def generate_network_diagram():
    """Generate a Mermaid network diagram comparing CDN and P2P/CDN topologies."""
    diagram = """
    graph TD
        %% Flat CDN Topology
        subgraph CDN["Flat CDN Topology"]
            Client1[Client 1] --> CDN1[CDN Edge 1]
            Client2[Client 2] --> CDN2[CDN Edge 2]
            Client3[Client 3] --> CDN3[CDN Edge 3]
            CDN1 --> Origin[Origin Server]
            CDN2 --> Origin
            CDN3 --> Origin
        end
        
        %% Hybrid P2P/CDN Topology
        subgraph Hybrid["Hybrid P2P/CDN Topology"]
            C1[Client 1] --> E1[Edge 1]
            C2[Client 2] --> E2[Edge 2]
            C3[Client 3] --> E3[Edge 3]
            E1 <--> E2
            E2 <--> E3
            E1 <--> E3
            E1 --> O[Origin]
            E2 --> O
            E3 --> O
        end
    """
    
    # Save the diagram to a file
    with open('network_diagram.mmd', 'w') as f:
        f.write(diagram)
    
    # Create an HTML file to display the Mermaid diagram
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script>
            mermaid.initialize({{ startOnLoad: true }});
        </script>
    </head>
    <body>
        <div class="mermaid">
        {diagram}
        </div>
    </body>
    </html>
    """
    
    with open('network_diagram.html', 'w') as f:
        f.write(html_content)
    
    # Open the HTML file in the default browser
    webbrowser.open('file://' + os.path.realpath('network_diagram.html'))

if __name__ == "__main__":
    plot_throughput_latency()
    generate_network_diagram()
    print("Visualizations generated: performance_plot.png and network_diagram.mmd")
    print("Opening network diagram in your default browser...") 