This directory should hold configuration files for custom mininets.

See custom_example.py, which loads the default minimal topology.  The advantage of defining a mininet in a separate file is that you then use the --custom option in mn to run the CLI or specific tests with it.

To start up a mininet with the provided custom topology, do:

```bash
sudo mn --custom topo-3h2s-ip.py --topo mytopo --controller=remote
```

### sFlow

添加 sFlow 流量监控

```bash
sudo mn --custom FatTree/fattree2-bw.py,sFlow/sflow.py --topo fattree,4 --mac --link tc --controller=remote
```

