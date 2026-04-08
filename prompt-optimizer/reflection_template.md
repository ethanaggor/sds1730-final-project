I am optimizing an AI agent that predicts U.S. state-level housing crash severity from pre-crisis economic indicators. The agent is implemented as a Recursive Language Model (RLM), an inference strategy where the input context (training and test DataFrames) is stored as external variables in a sandboxed Python REPL rather than fed directly into the LM's context window. The agent programmatically examines, decomposes, and queries over this data through iterative code execution (up to 20 rounds), optionally spawning sub-LM calls for semantic analysis, and calls SUBMIT() to return final predictions. The DSPy framework already injects REPL instructions, variable descriptions, available tools (llm_query, llm_query_batched, print, SUBMIT), iteration guidance, and the output JSON schema into the agent's context. You do not need to include any of that in your instruction.

The agent receives two DataFrames:
- train_df: ~40 states with columns [state, appreciation_03_06, ur_2006, pcpi_2006, pop_growth_03_06, crash_pct]
- test_df: ~11 held-out states with the same columns EXCEPT crash_pct (the target)

The agent must predict crash_pct for the test states using only the economic indicators and the training data. This is a cross-validation experiment testing whether an LLM agent can outperform OLS regression by combining domain reasoning with computation.

Here are the current instructions given to the agent:
```
<curr_instructions>
```

Below are examples of different task inputs provided to the agent, the agent's responses, and feedback on how the agent performed:
```
<inputs_outputs_feedback>
```

Your task is to write improved instructions for the agent.

WHAT TO OPTIMIZE:
- The agent's analytical strategy for predicting crash severity from the four economic indicators
- How the agent reasons about relationships between indicators and outcomes
- How the agent uses the training data to inform predictions for held-out states
- Computational approaches: weighting schemes, similarity metrics, regional pattern detection
- How the agent leverages its recursive capabilities (sub-LM calls for semantic analysis, iterative data exploration)

WHAT IS FORBIDDEN:
- Do NOT embed actual crash_pct values, historical outcome mappings, or state-specific results in the instruction. The feedback contains per-state errors for diagnostic purposes only. The agent must predict from indicators, not from memorized answers.
- Do NOT include REPL usage instructions, SUBMIT documentation, variable descriptions, tool documentation, or iteration guidance. The framework already provides these.
- Do NOT include output format specifications or JSON schemas. The framework handles this.

Read the feedback to understand where the agent's predictions are weakest (which types of states, which error patterns), then propose an instruction that improves the analytical strategy. Focus on reasoning methodology, not factual content.

Provide the new instructions within ``` blocks.
