#### special - local\share\check_mk\agents\special\agent_joey
- This is the script to run that should output data from an external API
- This does not evaluate a check result, it fetches data only
- This file should be executable and include a shebang
#### checks - local\share\check_mk\checks\agent_joey
- This passes arguments to the special agent file as defined in wato. Wato configurations are designed in the wato file
#### agent_based - local\lib\python3\cmk\base\plugins\agent_based\joey_agent.py
- This is the file that evaluates the output from the (special) agent, parses it, and determines a check result
- it determines how many services to derive from the agent output
- Agent output only comes from the agent section specified within this file
#### wato - local\share\check_mk\web\plugins\wato\joey_register.py
- This is the file that describes the discovery rules for executing this special agent_joey
- If discovery rules are not defined, the agent will not be executed against the host