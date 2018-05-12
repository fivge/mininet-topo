#!/usr/bin/env python

# usage: mn --custom <path to fattree.py> --topo fattree[,n] ...

"""Custom topology example

author: Haichen Shen (haichen@cs.washington.edu)

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host
"""

from mininet.topo import Topo

class FatTree( Topo ):
    "FatTree topology of depth 3."

    def __init__( self, half_ports = 2, **opts ):
        "Create custom topo."

        # Add default members to class.
        #super( FatTree, self ).__init__()
        Topo.__init__(self, **opts)

        aggrs = []
        hnum = 0
        snum = 0

        # Create Aggr switches
        for i in range(half_ports):
            snum += 1
            aggrs.append(self.addSwitch('s%s' % snum))
            
        # Create Tor switches
        for i in range(half_ports*2):
            snum += 1
            sw = self.addSwitch('s%s' % snum)

            # Connect Tor to Aggr
            for j in range(half_ports):
                self.addLink(sw, aggrs[j])

            # Create hosts and links
            for j in range(half_ports):
                hnum += 1
                host = self.addHost('h%s' % hnum)
                self.addLink(sw, host)

topos = { 'fattree': FatTree }
