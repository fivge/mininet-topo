This directory should hold configuration files for custom mininets.

See custom_example.py, which loads the default minimal topology.  The advantage of defining a mininet in a separate file is that you then use the --custom option in mn to run the CLI or specific tests with it.

To start up a mininet with the provided custom topology, do:

```bash
sudo mn --custom powersaving.py --topo mytopo --controller=remote
```

### sFlow

添加 sFlow 流量监控

```bash
sudo mn --custom sFlow/sflow.py,FatTree/fattree1.py --link tc,bw=10 --topo mytopo --controller=remote
```

