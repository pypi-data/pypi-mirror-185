# spikesafe-python

The official Python driver supporting Vektrex SpikeSafe products:
- [SpikeSafe SMU](https://www.vektrex.com/products/spikesafe-source-measure-unit/)
- [SpikeSafe Performance Series ("PRF")](https://www.vektrex.com/products/spikesafe-performance-series-precision-pulsed-current-sources/)

Vektrex SpikeSafe Python API used for automation of custom instrument control sequences for testing LED, laser, and electronic equipment.

The Vektrex SpikeSafe Python API powers the Python examples published on Github.

GitHub Repository: [SpikeSafe Python Samples](https://github.com/VektrexElectronicSystems/SpikeSafePythonSamples)

Library help documentation: [spikesafe_python_lib_docs](https://github.com/VektrexElectronicSystems/SpikeSafePythonSamples/tree/master/spikesafe_python_lib_docs)

## About

The **spikesafe-python** package provides light-weight access Python helper classes and functions to easily communicate with to your SpikeSafe and parse data into easy to use objects.

**spikesafe-python** supports all operating systems that support the free [Python](https://www.python.org/) interpreter.

**spikesafe-python** follows [Python Software Foundation](https://devguide.python.org/#status-of-python-branches) for supporting different versions.

## Installation

Install the latest stable version of **spikesafe-python** with [pip](http://pypi.python.org/pypi/pip):

```
$ python -m pip install spikesafe-python
```

## Usage

Easily connect to a SpikeSafe and read its identification:

```
from spikesafe_python.TcpSocket import TcpSocket

# create socket and connect to SpikeSafe
tcp_socket = TcpSocket()
tcp_socket.open_socket('10.0.0.220', 8282)

# request and read SpikeSafe identification
tcp_socket.send_scpi_command('*IDN?')
idn = tcp_socket.read_data()

print(idn)
```

Simply use a SpikeSafe to power on a 3V LED/laser for 10 seconds and read its voltage:

```
from spikesafe_python.MemoryTableReadData import MemoryTableReadData
from spikesafe_python.TcpSocket import TcpSocket
from spikesafe_python.Threading import wait

# create socket and connect to SpikeSafe
tcp_socket = TcpSocket()
tcp_socket.open_socket('10.0.0.220', 8282)

# set SpikeSafe current to 100 mA, compliance voltage to 10V, and turn it on 
tcp_socket.send_scpi_command('SOUR1:CURR 0.1')                                 
tcp_socket.send_scpi_command('SOUR1:VOLT 10')                           
tcp_socket.send_scpi_command('OUTP1 1')

# wait 10 seconds for LED/laser to power on
wait(10)           

# read and parse LED/laser data
data = tcp_socket.read_data()                                            
memory_table_read = MemoryTableReadData().parse_memory_table_read(data)

print(memory_table_read.channel_data[0].voltage_reading)
```

Connect to more than one SpikeSafe:

```
from spikesafe_python.TcpSocket import TcpSocket

# create socket and connect to SpikeSafe 1
spike_safe_1 = TcpSocket()
spike_safe_1.open_socket('10.0.0.220', 8282)

# create socket and connect to SpikeSafe 2
spike_safe_2 = TcpSocket()
spike_safe_2.open_socket('10.0.0.221', 8282)

```

## Support / Feedback

For further assistance with **spikesafe-python** please contact Vektrex support at support@vektrex.com. This page is regularly monitored and maintained by Vektrex engineers.

## Built With

* [Visual Studio Code](https://code.visualstudio.com/)
* [Python for Windows](https://www.python.org/downloads/windows/)

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Bill Thompson** - [BillThomp](https://github.com/BillThomp)
* **Eljay Gemoto** - [eljayg](https://github.com/eljayg)

## License

**spikesafe-python** is licensed under the MIT license, which allows for non-commercial and commercial use.