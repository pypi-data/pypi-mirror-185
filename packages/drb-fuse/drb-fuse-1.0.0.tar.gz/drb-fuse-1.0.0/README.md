# Drb Fuse Representation
This drb-fuse module implements a representation of DrbNode as a field system. It is able to navigates among the DrbNode 
contents.

## FsNode

FsNode is the node that implement the Fuse representation of a node.

An example that represent a xml node from the file test.xml on directory /tmp/hello/:

Create a FsNode with argument 'node' and 'mountpoint'
And after  sets up a fuse file system that represent the node.
The directory pointed by 'mountpoint' must exist

```python

from multiprocessing import Process
from drb.drivers.file import DrbFileFactory
from drb.fuse import FsNode

xml_file = "files" / "test.xml"
node_file = DrbFileFactory().create(xml_file)
fsnode = FsNode(node_file, '/tmp/hello/')

process_fs = Process(target=fsnode.run_fs(),
                     kwargs={'node': node, 'mountpoint': '/tmp/hello/'}
```

Same example with functions start_fs:
The function start_fs create the directory if the directory not exists
And create an instance of FsNode with  'node' and 'mountpoint'
and launch the method 'run_fs()' from the instance of FsNode

```python

from multiprocessing import Process
from drb.drivers.file import DrbFileFactory
from drb.fuse import FsNode
from drb.fuse.drb_fuse3 import start_fs

xml_file = "files" / "test.xml"

node_file = DrbFileFactory().create(xml_file)
process_fs = Process(target=start_fs,
                     kwargs={'node': node, 'mountpoint': '/tmp/hello/'}
```

## Using this module

To include this module into your project, the `drb-fuse` module shall be referenced into `requirement.txt` file, or
the following pip line can be run:
```commandline
pip install drb-fuse
```

The fuse3 library have to be installed 

For ubuntu the following command line can be run:
```commandline
sudo apt install fuse3 libfuse3-dev
```




