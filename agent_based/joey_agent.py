#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) Andreas Doehler <andreas.doehler@bechtle.com/andreas.doehler@gmail.com>

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# <<<ilo_api_general:sep(124)>>>
# ProLiant DL380 Gen10|U30 v2.04 (04/18/2019)|CZ123456789|OK
# Server Typ | BIOS Ver. | Serial | Health

from .agent_based_api.v1.type_defs import (
    CheckResult,
    DiscoveryResult,
)

from .agent_based_api.v1 import *

import random

# The name of the agent section from our special agent output, this is only needed if you have a custom output parser
register.agent_section(
    name="joey_agent_section",
)

# Just yield as many services as we want from the output of the agent section
# Here we just yield a service for each line outputted from our section of the special agent. The item gets passed to the check function and as a string value to the service
# name in the register.check_plugin service_name parameter
def discovery_joey_agent(section) -> DiscoveryResult:
    for line in section:
        yield Service(item=line[0])


# Remove the item argument if its a single service check, this runs one time for each service yielded from the discovery function
def check_joey_agent(item, section) -> CheckResult:
    # Performance metrics are optional but will be graphed as the are recorded
    # https://docs.checkmk.com/latest/en/devel_check_plugins.html#_performance_values
    perfValue = random.randrange(0, 100)
    yield Metric('importantvalue', perfValue, levels=(90,96))
    # You can yield multiple results https://docs.checkmk.com/latest/en/devel_check_plugins.html#_checks_with_multiple_partial_results
    yield Result(
        state=State.OK, # Return State.OK, State.WARN, State.CRIT
        summary="Sweeeeet thanks "+item) # Summary should be less then 60 chars to provide a overview of state
        #notice="Check went great heres a bunch of info on how it went!") # Notice is extra details https://docs.checkmk.com/latest/en/devel_check_plugins.html#_summary_and_details
    return # Always return just to make sure the function completes


register.check_plugin(
    name="joey_agent",
    service_name="Joeys Special Status for %s",
    sections=["joey_agent_section"],
    discovery_function=discovery_joey_agent,
    check_function=check_joey_agent,
)