
# **CarbonIQ**

**CarbonIQ** is a Python package that monitors and tracks the carbon emissions of scripts and applications. It provides insights into the environmental impact of code by analyzing resource usage such as CPU, memory, disk I/O, network, and GPU utilization.

---

## **Key Features**
- **Comprehensive Resource Tracking**:
  - Tracks energy usage for CPU, memory, disk, and network I/O.
  - Monitors GPU resource utilization via NVIDIA Management Library (NVML).

- **Real-Time Emission Factor Integration**:
  - Dynamically fetches carbon intensity data with live updates (optional).

- **Detailed Execution Summaries**:
  - Generates energy consumption breakdowns and carbon emissions estimates.
  - Includes a gamified badge system to encourage eco-friendly development.

- **Flexible Integration**:
  - Supports usage in functions, API calls, and entire workflows.

- **Platform-Agnostic**:
  - Works seamlessly across operating systems with Python 3.6+.

---

## **Installation**
Install CarbonIQ using `pip`:

```bash
pip install carboniq
```

To disable dependency caching during installation:

```bash
pip install --no-cache-dir carboniq
```

---

## **Usage**

### **1. Profiling a Function**
Wrap your function with the `@carbon_profiler` decorator to profile its resource usage:

```python
from carboniq.emissions import carbon_profiler

@carbon_profiler(real_time=True)
def example_function():
    # Perform a computationally heavy task
    result = sum(i ** 2 for i in range(1000000))
    return result

example_function()
```

---

### **2. Profiling an API Call**
Use the decorator for profiling API requests to measure their environmental footprint:

```python
from carboniq.emissions import carbon_profiler
import requests

@carbon_profiler(real_time=True)
def fetch_data_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()

fetch_data_from_api()
```

---

### **3. Profiling a Workflow**
CarbonIQ can also profile loops or workflows, such as while loops or batch operations:

```python
from carboniq.emissions import carbon_profiler

@carbon_profiler(real_time=False)
def batch_processing():
    count = 0
    while count < 5:
        # Simulate a task
        print(f"Processing batch {count + 1}")
        count += 1

batch_processing()
```

---

### **4. Profiling Real-Time Tasks**
CarbonIQ is effective for long-running tasks like monitoring server performance:

```python
from carboniq.emissions import carbon_profiler
import time

@carbon_profiler(real_time=True)
def monitor_server():
    print("Monitoring server resources...")
    time.sleep(10)  # Simulate a 10-second monitoring task

monitor_server()
```

---

### **Real-Time Emissions Tracking**
To enable real-time tracking of carbon emissions using live grid intensity data:
1. Use the `real_time=True` argument in the `@carbon_profiler` decorator.
2. Ensure an active internet connection for fetching live emission factors from the [ElectricityMap API](https://electricitymap.org/).

---

## **System Requirements**
- **Python Version**: 3.6 or higher.
- **Optional NVIDIA GPU Tracking**:
  - Requires the `pynvml` library and NVIDIA drivers.
---

## **Contributing**
We welcome contributions to CarbonIQ! To contribute:
1. Fork the repository: [CarbonIQ Repository](https://github.com/ashikrafi/CarbonIQ).
2. Create a new branch for your feature or bug fix.
3. Submit a pull request detailing your changes.

---

## **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## **Contact**
**Author**: Md Ashikur Rahman  
**Email**: [mdashikur.rafi@gmail.com](mailto:mdashikur.rafi@gmail.com)  
**GitHub**: [ashikrafi](https://github.com/ashikrafi)

---

By integrating CarbonIQ into your development process, you contribute to sustainable software practices and reduce the environmental impact of your applications.
