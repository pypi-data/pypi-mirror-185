# lcmlog-py

LCM log utilities

## Installation

`lcmlog-py` is available on PyPI:

```bash
pip install lcmlog-py
```

## Usage

### Events

`lcmlog-py` provides classes to abstract the LCM log file format. The `Event` class represents a single event in the log file. An `Event` is composed of a header, channel string, and data byte array.

The `Header` class represents a fixed-length header at the beginning of each event which describes the event number, timestamp, and channel/data lengths. This is parsed first, and then the channel and data are read in.

If the header is read incorrectly or is corrupt, a `BadSyncError` is raised.

To read a header, call the `Header.from_file` method:

```python
from lcmlog import Header

with open('lcmlog', 'rb') as f:
    header = Header.from_file(f)

print(header.timestamp)  # e.g.
```

A full event can be read via the `Event.from_file` method:

```python
from lcmlog.event import Event

with open('lcmlog', 'rb') as f:
    event = Event.from_file(f)

print(event.header.timestamp)
print(event.channel)  # e.g.
```

### Log Reader & Writer

`lcmlog-py` also provides two utility classes for reading and writing LCM log files in order.

The `LogReader` reads events from a file (starting at the beginning) and the `LogWriter` writes events to a file. The `LogReader` class is iterable. Both classes close their respective files when they are garbage collected.

```python
from lcmlog import LogReader, LogWriter

reader = LogReader('lcmlog_source')
writer = LogWriter('lcmlog_dest')

# Read and write each event
for event in reader:
    writer.write(event)
```