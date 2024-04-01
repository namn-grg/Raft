# Raft
Implementing a modified Raft system similar to those used by geo-distributed Database clusters such as CockroachDB or YugabyteDB. Raft is a consensus algorithm designed for distributed systems to ensure fault tolerance and consistency. It operates through leader election, log replication, and commitment of entries across a cluster of nodes.

We aim to build a database that stores key-value pairs mapping string (key) to string (value). The Raft cluster maintains this database and ensures fault tolerance and strong consistency. The client requests the server to perform operations on this database reliably.

## Leader Lease
It is possible to rely on a time-based “lease” for Raft leadership that gets propagated through the heartbeat mechanism. And if we have well-behaved clocks, we can obtain linearizable reads without paying a round-trip latency penalty. This is achieved using the concept of Leases.

## Demo


## Test scenario

0. Start the cluster with 5 nodes. Wait for the leader to be elected and a NO-OP entry to be appended in all the logs.
   [Leader Election]

1. Have the client perform 3 set requests and then 3 get requests. Verify if the set request has been replicated in each log. Get requests should be returned immediately without any additional heartbeats by the leader. [Log Replication, Basic Functionality]

2. Terminate one or two of the follower nodes and perform 3 SET requests and 3 GET requests. Restart the terminated followers. Verify if the terminated follower rejoins the cluster with updated logs and state. [Fault Tolerance, Follower Catch-up]

3. Terminate the current leader process. Wait for the new leader to be elected & perform 2 set and 2 get requests. Restart the terminated (old leader) process. Verify if a new leader is elected & cluster continues operation without data loss in the logs. Also, ensure the old leader node should join the cluster as a follower with an updated state. [Fault Tolerance, Leader Failure, Leader Election, Log Replication]

4. Terminate 3 (majority) follower nodes, and before the lease times out, send a Get request to the leader. Also, observe if the leader’s lease times out after some time and the leader steps down to become a follower node. The leader should be able to return the correct value for the GET request if it's within the lease interval. Timing is crucial, and the dump.txt can verify if the request was received timely. The lease should also time-out since the leader can't reach any of the follower nodes. [O(1) Read Request, Leader Lease Timeout]

5. Terminate all the nodes except two follower nodes, send a Get and Set request to any of the followers. Both Get and Set requests should fail ultimately as there is no leader present in the system. No node will be able to become the leader. [Failure in absence of leader in the system]

Note: We will not be checking network partitions explicitly as it is difficult to simulate a network partition without any hard-coding or changes to the default algorithm. But the above test case scenarios cover most of the aspects related to network partition.

Assumptions

You need only to create one cluster of the database using Raft. This cluster contains multiple nodes, but the number of nodes can remain fixed from the start (nodes need not be dynamically added or removed).
You can use interrupts to stop a node/program (for example, Ctrl+C to stop the process). To emulate restarting the node, the program for the node will be executed again.
