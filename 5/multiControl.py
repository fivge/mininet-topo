#!/usr/bin/python

"""
Script created by VND - Visual Network Description (SDN version)
"""
import time
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def topology():
    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24' )
    h3 = net.addHost( 'h3', mac='00:00:00:00:00:03', ip='10.0.0.3/24' )
    h4 = net.addHost( 'h4', mac='00:00:00:00:00:04', ip='10.0.0.4/24' )
    s1 = net.addSwitch( 's1', protocols='OpenFlow13', listenPort=6653, mac='00:00:00:00:00:05' )
    s2 = net.addSwitch( 's2', protocols='OpenFlow13', listenPort=6653, mac='00:00:00:00:00:06' )
    s3 = net.addSwitch( 's3', protocols='OpenFlow13', listenPort=6653, mac='00:00:00:00:00:07' )
    s4 = net.addSwitch( 's4', protocols='OpenFlow13', listenPort=6653, mac='00:00:00:00:00:08' )
    c0 = net.addController( 'controller1', controller=RemoteController, ip='192.168.234.130', port=6653 )
    c1 = net.addController( 'controller2', controller=RemoteController, ip='192.168.234.131', port=6653 )

    print "*** Creating links"
    net.addLink(h1, s1, 0, 1)
    net.addLink(h2, s1, 0, 2)
    net.addLink(h3, s4, 0, 1)
    net.addLink(h4, s4, 0, 2)
    net.addLink(s1, s2, 3, 1)
    net.addLink(s1, s3, 4, 1)
    net.addLink(s4, s2, 3, 2)
    net.addLink(s4, s3, 4, 2)

    print "*** Starting network"
    net.build()
    c0.start()
    c1.start()
    s4.start( [c0] )
    s3.start( [c0] )
    s2.start( [c1] )
    s1.start( [c1] )

    net.start()
    
    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
