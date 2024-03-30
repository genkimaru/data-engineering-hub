---
title: Full Load
weight: 148
---


With a full load, the entire dataset is dumped, or loaded, and is then completely replaced (i.e., deleted and replaced) with the new, updated dataset. No additional information, such as timestamps, is required.

## Full Load Advantages

- Easy to build and maintain
	- A full load won't require you to manage the keys and even if some data is up to date or not, it won't matter since **all** the data will be updated.
- Simple design
	- No need to worry about database design. For example, new records that would otherwise invalidate existing data (giving an integer to a column that expects text) don't need to be considered.


## Full Load Disadvantages

- Resource and time inefficient
	- Deciding to do a full load on larger datasets will take a great amount of time and other server resources. Ideally, all the data loads are performed overnight with the exception of completing them before users can see the data the next day. There might not be enough time during the overnight window for the full load to complete.
- Preserving history
	- When dealing with a OLTP source that is not designed to keep history, a full load will remove history from the destination as well, since a full load removes all the records first.
- Not scalable
	- It can be an inconvenience to load data when only a handful of records need to be updated but millions of records have to be loaded due to the nature of a full load having to update **all** the records each time.

