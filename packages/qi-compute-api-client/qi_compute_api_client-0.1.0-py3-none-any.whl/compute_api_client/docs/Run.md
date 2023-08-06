# Run


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_on** | **datetime** |  | [readonly] 
**queued_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**id** | **int** |  | 
**algorithm_type** | [**AlgorithmType**](AlgorithmType.md) | HYBRID: hybrid&lt;br/&gt;QUANTUM: quantum | 
**status** | [**RunStatus**](RunStatus.md) | PLANNED: planned&lt;br/&gt;RUNNING: running&lt;br/&gt;COMPLETED: completed&lt;br/&gt;CANCELLED: cancelled&lt;br/&gt;FAILED: failed | 
**batch_run_id** | **int** |  | 
**file_id** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


