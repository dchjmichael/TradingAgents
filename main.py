from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
import os

# Create a custom config
config = DEFAULT_CONFIG.copy()
# config["llm_provider"] = "google"  # Use a different model
config["llm_provider"] = "deepseek"  # Use a different model
# config["backend_url"] = "https://generativelanguage.googleapis.com/v1"  # Use a different backend
config["backend_url"] = "https://api.deepseek.com/v1"  # Use a different backend
# config["deep_think_llm"] = "gemini-2.0-flash"  # Use a different model
config["deep_think_llm"] = "deepseek-reasoner"  # Use a different model
# config["quick_think_llm"] = "gemini-2.0-flash"  # Use a different model
config["quick_think_llm"] = "deepseek-chat"  # Use a different model
config["max_debate_rounds"] = 1  # Increase debate rounds
config["online_tools"] = True  # Increase debate rounds

os.environ["DEEPSEEK_API_KEY"] = "sk-e9e79e385a8541b5a604ccefaa0c991c"
os.environ["OPENAI_API_KEY"] = "sk-e9e79e385a8541b5a604ccefaa0c991c"


# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2025-05-01")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
