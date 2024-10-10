[[EBS (Elastic Block Store)]]
1. Backup of our EBS volume at specific point -> snapshot
2. Recommended to detach volume to do snapshot
3. Can copy snapshots across AZ or region -> move around global infra
4. US-East-1a -> US-East-1b ( we have EBS A -> Snapshot EBS -> can be used as EBS B) snapshot and restore mechanism

##### EBS Snapshot Features
1. EBS Snapshot Archive
	1. Move snapshot to "archive tier" -> 75% cheaper
	2. Take around 24-72 hours to restore archive
	3. cannot be rushed, slow progress, but cheap
	
2. Recycle Bin for EBS Snapshot
	1. Recover snapshots after accidental deletion
	2. Specify retention ( 1 day - 1 year )

