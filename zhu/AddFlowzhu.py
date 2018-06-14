#!/usr/bin/python
# coding: utf-8

import httplib  
import json
  
class StaticFlowPusher(object):  
  
    def __init__(self, server):  
        self.server = server  
  
    def get(self, data):  
        ret = self.rest_call({}, 'GET')  
        return json.loads(ret[2])  
  
    def set(self, data):  
        ret = self.rest_call(data, 'POST')  
        return ret[0] == 200  
  
    def remove(self, objtype, data):  
        ret = self.rest_call(data, 'DELETE')  
        return ret[0] == 200  
  
    def rest_call(self, data, action):  
        #path = '/wm/staticflowentrypusher/json'
        path = '/wm/staticflowpusher/json'
        #path = '/wm/staticentrypusher/json'  
        headers = {  
            'Content-type': 'application/json',  
            'Accept': 'application/json',  
            }  
        body = json.dumps(data)  
        conn = httplib.HTTPConnection(self.server, 8080)
        print conn  
        conn.request(action, path, body, headers)  
        response = conn.getresponse()  
        ret = (response.status, response.reason, response.read())  
        print ret  
        conn.close()  
        return ret	
pusher = StaticFlowPusher('127.0.0.1')

#switch[00:00:00:00:00:00:00:01]
en_group_0 = {
    "switch":"00:00:00:00:00:00:00:01",
    "entry_type" : "group",
    "name" : "group-mod-0",
    "active" : "true",
    "group_type" : "fast_failover",
    "group_id" : "1",
    "group_buckets":[ 
        {
	"bucket_id" : "1",
        "bucket_watch_port" : "4",
        "bucket_actions":"output=4"
        },
        {
        "bucket_id" : "2",
        "bucket_watch_port" : "3", 
        "bucket_actions" : "push_mpls=0x8847,set_field=mpls_label->0x10,output=3"
        }]}
pusher.set(en_group_0)

flow_1_arp_01 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-01-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:01",
    "eth_dst":"ff:ff:ff:ff:ff:ff",
    "active":"true",
    "instruction_apply_actions":"group=1"
}
pusher.set(flow_1_arp_01)

flow_1_arp_02 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-02-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:02",
    "eth_dst":"ff:ff:ff:ff:ff:ff",
    "active":"true",
    "instruction_apply_actions":"group=1"
}
pusher.set(flow_1_arp_02)

flow_1_arp_1 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-1-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_dst":"00:00:00:00:00:01",
    "active":"true",
    "actions":"output=1"
}
pusher.set(flow_1_arp_1)

flow_1_arp_2 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-2-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_dst":"00:00:00:00:00:02",
    "active":"true",
    "actions":"output=2"
}
pusher.set(flow_1_arp_2)

flow_1_arp_3 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-3-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_dst":"00:00:00:00:00:03",
    "active":"true",
    "instruction_apply_actions":"group=1"
}
pusher.set(flow_1_arp_3)

flow_1_arp_4 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-4-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_dst":"00:00:00:00:00:04",
    "active":"true",
    "instruction_apply_actions":"group=1"
}
pusher.set(flow_1_arp_4)

flow_1_ip_0 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-t1-ip",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.1",
    "active":"true",
    "actions":"output=1"
}
pusher.set(flow_1_ip_0)

flow_1_ip_1 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-t2-ip",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.2",
    "active":"true",
    "actions":"output=2"
}
pusher.set(flow_1_ip_1)

en_group_1 = {
    "switch":"00:00:00:00:00:00:00:01",
    "entry_type" : "group",
    "name" : "group-mod-1",
    "active" : "true",
    "group_type" : "fast_failover",
    "group_id" : "2",
    "group_buckets":[ 
        {
	"bucket_id" : "1",
        "bucket_watch_port" : "4",
        "bucket_actions":"output=4"
        },
        {
        "bucket_id" : "2",
        "bucket_watch_port" : "3", 
        "bucket_actions" : "push_mpls=0x8847,set_field=mpls_label->0x11,output=3"
        }]}
pusher.set(en_group_1)

flow_1_ip_2 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-t3-ip",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.3",
    "active":"true",
    "instruction_apply_actions":"group=2"
}
pusher.set(flow_1_ip_2)

flow_1_ip_3 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow-1-t4-ip",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.4",
    "active":"true",
    "instruction_apply_actions":"group=2"
}
pusher.set(flow_1_ip_3)

flow_1_fail_0 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_1_fail_0",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x8847",
    "active":"true",
    "instruction_apply_actions":"output=3"
}
pusher.set(flow_1_fail_0)

#--------------------------------------------------------------------------------------

#switch[00:00:00:00:00:00:00:03]
en_group_3_1 = {
    "switch":"00:00:00:00:00:00:00:03",
    "entry_type" : "group",
    "name" : "group-mod-3-1",
    "active" : "true",
    "group_type" : "fast_failover",
    "group_id" : "3",
    "group_buckets":[ 
        {
	"bucket_id" : "1",
        "bucket_watch_port" : "1",
        "bucket_actions":"output=1"
        },
        {
        "bucket_id" : "2",
        "bucket_watch_port" : "2", 
        "bucket_actions" : "push_mpls=0x8847,set_field=mpls_label->0x10,output=in_port"
        }]}
pusher.set(en_group_3_1)

en_group_3_2 = {
    "switch":"00:00:00:00:00:00:00:03",
    "entry_type" : "group",
    "name" : "group-mod-3-2",
    "active" : "true",
    "group_type" : "fast_failover",
    "group_id" : "4",
    "group_buckets":[ 
        {
	"bucket_id" : "1",
        "bucket_watch_port" : "2",
        "bucket_actions":"output=2"
        },
        {
        "bucket_id" : "2",
        "bucket_watch_port" : "1", 
        "bucket_actions" : "push_mpls=0x8847,set_field=mpls_label->0x10,output=in_port"
        }]}
pusher.set(en_group_3_2)

flow_3_arp_0 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow-3-tleft-arp",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "eth_type":"0x0806",
    "active":"true",
    "instruction_apply_actions":"group=4"
}
pusher.set(flow_3_arp_0)

flow_3_arp_1 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow-3-tright-arp",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "eth_type":"0x0806",
    "active":"true",
    "instruction_apply_actions":"group=3"
}
pusher.set(flow_3_arp_1)

en_group_3_3 = {
    "switch":"00:00:00:00:00:00:00:03",
    "entry_type" : "group",
    "name" : "group-mod-3-3",
    "active" : "true",
    "group_type" : "fast_failover",
    "group_id" : "5",
    "group_buckets":[ 
        {
	"bucket_id" : "1",
        "bucket_watch_port" : "1",
        "bucket_actions":"output=1"
        },
        {
        "bucket_id" : "2",
        "bucket_watch_port" : "2", 
        "bucket_actions" : "push_mpls=0x8847,set_field=mpls_label->0x11,output=in_port"
        }]}
pusher.set(en_group_3_3)

en_group_3_4 = {
    "switch":"00:00:00:00:00:00:00:03",
    "entry_type" : "group",
    "name" : "group-mod-3-4",
    "active" : "true",
    "group_type" : "fast_failover",
    "group_id" : "6",
    "group_buckets":[ 
        {
	"bucket_id" : "1",
        "bucket_watch_port" : "2",
        "bucket_actions":"output=2"
        },
        {
        "bucket_id" : "2",
        "bucket_watch_port" : "1", 
        "bucket_actions" : "push_mpls=0x8847,set_field=mpls_label->0x11,output=in_port"
        }]}
pusher.set(en_group_3_4)

flow_3_ip_0 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow-2-tleft-ip",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "eth_type":"0x0800",
    "active":"true",
    "instruction_apply_actions":"group=6"
}
pusher.set(flow_3_ip_0)

flow_3_ip_1 = {
    'switch':"00:00:00:00:00:00:00:03",
    "name":"flow-3-tright-ip",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "eth_type":"0x0800",
    "active":"true",
    "instruction_apply_actions":"group=5"
}
pusher.set(flow_3_ip_1)

#--------------------------------------------------------------------------------------

#switch[00:00:00:00:00:00:00:02]
flow_2_arp_0 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow-2-tleft-arp",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "eth_type":"0x8847",
    "mpls_label":"0x10",
    "active":"true",
    "actions":"pop_mpls=0x0806,output=2"
}
pusher.set(flow_2_arp_0)

flow_2_arp_1 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow-2-tright-arp",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "eth_type":"0x8847",
    "mpls_label":"0x10",
    "active":"true",
    "actions":"pop_mpls=0x0806,output=1"
}
pusher.set(flow_2_arp_1)

flow_2_ip_0 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow-2-tleft-ip",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "eth_type":"0x8847",
    "mpls_label":"0x11",
    "active":"true",
    "actions":"pop_mpls=0x0800,output=2"
}
pusher.set(flow_2_ip_0)

flow_2_ip_1 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow-2-tright-ip",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "eth_type":"0x8847",
    "mpls_label":"0x11",
    "active":"true",
    "actions":"pop_mpls=0x0800,output=1"
}
pusher.set(flow_2_ip_1)

#--------------------------------------------------------------------------------------

#switch[00:00:00:00:00:00:00:04]---
en_group_4_0 = {
    "switch":"00:00:00:00:00:00:00:04",
    "entry_type" : "group",
    "name" : "group-mod-4-0",
    "active" : "true",
    "group_type" : "fast_failover",
    "group_id" : "7",
    "group_buckets":[ 
        {
	"bucket_id" : "1",
        "bucket_watch_port" : "1",
        "bucket_actions":"output=1"
        },
        {
        "bucket_id" : "2",
        "bucket_watch_port" : "2", 
        "bucket_actions" : "push_mpls=0x8847,set_field=mpls_label->0x10,output=2"
        }]}
pusher.set(en_group_4_0)

en_group_4_1 = {
    "switch":"00:00:00:00:00:00:00:04",
    "entry_type" : "group",
    "name" : "group-mod-4-1",
    "active" : "true",
    "group_type" : "fast_failover",
    "group_id" : "8",
    "group_buckets":[ 
        {
	"bucket_id" : "1",
        "bucket_watch_port" : "1",
        "bucket_actions":"output=1"
        },
        {
        "bucket_id" : "2",
        "bucket_watch_port" : "2", 
        "bucket_actions" : "push_mpls=0x8847,set_field=mpls_label->0x11,output=2"
        }]}
pusher.set(en_group_4_1)

flow_4_arp_01 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-01-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:03",
    "eth_dst":"ff:ff:ff:ff:ff:ff",
    "active":"true",
    "instruction_apply_actions":"group=7"
}
pusher.set(flow_4_arp_01)

flow_4_arp_02 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-02-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:04",
    "eth_dst":"ff:ff:ff:ff:ff:ff",
    "active":"true",
    "instruction_apply_actions":"group=7"
}
pusher.set(flow_4_arp_02)

flow_4_arp_1 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-1-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_dst":"00:00:00:00:00:03",
    "active":"true",
    "actions":"output=3"
}
pusher.set(flow_4_arp_1)

flow_4_arp_2 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-2-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_dst":"00:00:00:00:00:04",
    "active":"true",
    "actions":"output=4"
}
pusher.set(flow_4_arp_2)

flow_4_arp_3 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-3-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_dst":"00:00:00:00:00:01",
    "active":"true",
    "instruction_apply_actions":"group=7"
}
pusher.set(flow_4_arp_3)
flow_4_arp_4 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-4-arp",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0806",
    "eth_dst":"00:00:00:00:00:02",
    "active":"true",
    "instruction_apply_actions":"group=7"
}
pusher.set(flow_4_arp_4)

flow_4_arp_03 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-03-arp",
    "cookie":"0",
    "priority":"32767",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:01",
    "eth_dst":"ff:ff:ff:ff:ff:ff",
    "active":"true",
    "actions":"output=1,output=2"
}
pusher.set(flow_4_arp_03)

flow_4_arp_04 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-04-arp",
    "cookie":"0",
    "priority":"32767",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:02",
    "eth_dst":"ff:ff:ff:ff:ff:ff",
    "active":"true",
    "actions":"output=1,output=2"
}
pusher.set(flow_4_arp_04)

flow_4_ip_0 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-t3-ip",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.3",
    "active":"true",
    "actions":"output=3"
}
pusher.set(flow_4_ip_0)

flow_4_ip_1 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-t4-ip",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.4",
    "active":"true",
    "actions":"output=4"
}
pusher.set(flow_4_ip_1)

flow_4_ip_2 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-t1-ip",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.1",
    "active":"true",
    "instruction_apply_actions":"group=8"
}
pusher.set(flow_4_ip_2)

flow_4_ip_3 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow-4-t2-ip",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.2",
    "active":"true",
    "instruction_apply_actions":"group=8"
}
pusher.set(flow_4_ip_3)

flow_4_fail_0 = {
    'switch':"00:00:00:00:00:00:00:04",
    "name":"flow_4_fail_0",
    "cookie":"0",
    "priority":"32768",
    "eth_type":"0x8847",
    "active":"true",
    "instruction_apply_actions":"output=2"
}
pusher.set(flow_4_fail_0)
