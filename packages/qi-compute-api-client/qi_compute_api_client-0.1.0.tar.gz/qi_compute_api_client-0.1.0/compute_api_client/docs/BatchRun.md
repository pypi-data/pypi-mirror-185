# BatchRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **datetime** |  | [readonly] 
**queued_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**id** | **int** |  | 
**status** | [**BatchRunStatus**](BatchRunStatus.md) | PLANNED: planned&lt;br/&gt;QUEUED: queued&lt;br/&gt;RESERVED: reserved&lt;br/&gt;RUNNING: running&lt;br/&gt;FINISHED: finished | 
**reserved_at** | **datetime** |  | [optional] 
**runtime_id** | **int** |  | [optional] 
**runtime_type_id** | **int** |  | 
**user_id** | **int** |  | 
**run_ids** | **list[int]** |  | 
**aggregated_algorithm_type** | [**AlgorithmType**](AlgorithmType.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


