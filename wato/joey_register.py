#!/usr/bin/env python3

#import required to register agent
from cmk.gui.plugins.wato import (
    IndividualOrStoredPassword,
    RulespecGroup,
    monitoring_macro_help,
    rulespec_group_registry,
    rulespec_registry,
    HostRulespec,
)
#import structure where special agent will be registered
from cmk.gui.plugins.wato.datasource_programs import RulespecGroupDatasourcePrograms

#Some WATO form definition, to ask user for port number
def _valuespec_special_agent_myspecial():
    return Dictionary(
        title=_("Joeys Agent WATO Title"),
        help=_("This agent sucks"),
        optional_keys=[],
        elements=[
            ("who", TextAscii(title=_("Who"), allow_empty=False)),
        ]
    )


#In that piece of code we registering Special Agent
rulespec_registry.register(
    HostRulespec(
        group=RulespecGroupDatasourcePrograms,
        #IMPORTANT, name must follow special_agents:<name>, 
        #where filename of our special agent located in path local/share/check_mk/agents/special/ is  agent_<name>
        name="special_agents:joey",
        valuespec=_valuespec_special_agent_myspecial,
    ))
    