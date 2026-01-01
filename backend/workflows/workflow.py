from agents.planner import planner_agent
from agents.coder import coder_agent
from agents.reviewer import reviewer_agent

def run_workflow(goal):
    plan = planner_agent(goal)
    code = coder_agent(plan)
    verified_code = reviewer_agent(goal, code)
    return verified_code
