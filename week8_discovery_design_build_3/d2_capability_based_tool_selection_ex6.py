# Tags each tool from d2_enterprise_tool_registry_ex5.py with a
# read/write capability and picks a tool by matching capability instead
# of by name — a coarse access-control layer on tool selection.
tools = {
    "get_customer": {"capability": "read"},
    "create_ticket": {"capability": "write"},
}

def select_tool(task_type):
    for tool, meta in tools.items():
        if meta["capability"] == task_type:
            return tool
    return None

print(select_tool("read"))