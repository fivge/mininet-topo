### FatTree Topo

```bash
# fattree1
sudo mn --custom fattree1.py --topo mytopo --mac --link tc  --controller=remote

### 可指定带宽bw
sudo mn --custom fattree1.py --topo mytopo --mac --link tc,bw=10  --controller=remote

# fattree2 
sudo mn --custom fattree2.py --topo fattree,4 --mac --link tc --controller=remote
```

