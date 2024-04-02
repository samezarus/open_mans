with 
	tabs as ( 
		select 
			key "tab_key", 
			value "tab_value"
		from
			app_checklists_checklisttest, jsonb_each(j_body -> 'tabs')
	),
	blocks as (
		select
			tabs.tab_key,
			tabs.tab_value,
			key "block_name", 
			value "block_value"
		from 
			tabs, jsonb_each(tab_value -> 'blocks')
	),
	items as (
		select
			tab_key,
			tab_value,
			block_name,
			block_value,
			key "items_key",
			value "items_value"
		from 
			blocks, jsonb_each(block_value -> 'items')
	),
	clients as (
		select
			tab_key,
			tab_value,
			block_name,
			block_value,
			items_value,
			items_value,
			value "clients_value"
		from 
			items, jsonb_array_elements(items.items_value -> 'clients') element
	)
select 
	* 
from 
	clients
where
	clients.clients_value -> 'val' = '0'





