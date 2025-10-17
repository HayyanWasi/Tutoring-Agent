import os
import json
from agents import function_tool
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner
import asyncio
import sys
import os

# Add paths
sys.path.append(os.path.join(os.path.dirname(__file__), 'class_09'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'class_10'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'class_11'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'class_12'))

# Import config - adjust path as needed
from Config.config import config

# Initialize agent mapping
agent_mapping = {'config': config}

# Import Class 09 Agents with error handling
# CLASS 11 AGENTS
try:
    from class_11.math_quiz_system_11.math_quiz_agent_11 import math_quiz_agent_11 as math_11
    agent_mapping.update({
        '11 math': math_11, '11 mathematics': math_11, 'class 11 math': math_11
    })
    print("✓ Math 11 imported")
except ImportError as e:
    print(f"✗ Math 11 import failed: {e}")

try:
    from class_11.physics_quiz_system_11.physics_quiz_agent_11 import physics_quiz_agent_11 as physics_11
    agent_mapping.update({
        '11 physics': physics_11, 'class 11 physics': physics_11
    })
    print("✓ Physics 11 imported")
except ImportError as e:
    print(f"✗ Physics 11 import failed: {e}")

# FIXED: Chemistry 11 - Correct file name
try:
    from class_11.chemistry_quiz_system_11.chemistry_quiz_agent_11 import chemistry_quiz_agent_11 as chemistry_11
    agent_mapping.update({
        '11 chemistry': chemistry_11, 'class 11 chemistry': chemistry_11
    })
    print("✓ Chemistry 11 imported")
except ImportError as e:
    print(f"✗ Chemistry 11 import failed: {e}")

try:
    from class_11.botany_quiz_system.botany_quiz_agent_11 import botany_quiz_agent_11 as botany_11
    agent_mapping.update({
        '11 botany': botany_11, 'class 11 botany': botany_11
    })
    print("✓ Botany 11 imported")
except ImportError as e:
    print(f"✗ Botany 11 import failed: {e}")

try:
    from class_11.zoology_quiz_system.zoology_quiz_agent_11 import zoology_quiz_agent_11 as zoology_11
    agent_mapping.update({
        '11 zoology': zoology_11, 'class 11 zoology': zoology_11
    })
    print("✓ Zoology 11 imported")
except ImportError as e:
    print(f"✗ Zoology 11 import failed: {e}")

try:
    from class_11.computer_quiz_system.computer_quiz_agent_11 import computer_quiz_agent_11 as computer_11
    agent_mapping.update({
        '11 computer': computer_11, 'class 11 computer': computer_11, '11 cs': computer_11
    })
    print("✓ Computer 11 imported")
except ImportError as e:
    print(f"✗ Computer 11 import failed: {e}")

try:
    from class_11.english_quiz_system_11.english_quiz_agent import english_quiz_agent_11 as english_11
    agent_mapping.update({
        '11 english': english_11, 'class 11 english': english_11
    })
    print("✓ English 11 imported")
except ImportError as e:
    print(f"✗ English 11 import failed: {e}")

# CLASS 12 AGENTS
try:
    from class_12.math_quiz_system_12.math_quiz_agent_11 import math_quiz_agent_11 as math_12
    agent_mapping.update({
        '12 math': math_12, '12 mathematics': math_12, 'class 12 math': math_12
    })
    print("✓ Math 12 imported")
except ImportError as e:
    print(f"✗ Math 12 import failed: {e}")

# FIXED: Physics 12 - Correct file name
try:
    from class_12.physics_quiz_system_12.physics_quiz_agent_12 import physics_quiz_agent_12 as physics_12
    agent_mapping.update({
        '12 physics': physics_12, 'class 12 physics': physics_12
    })
    print("✓ Physics 12 imported")
except ImportError as e:
    print(f"✗ Physics 12 import failed: {e}")

# FIXED: Chemistry 12 - Correct file name
try:
    from class_12.chemistry_quiz_system_12.chemistry_quiz_agent_12 import chemistry_quiz_agent_12 as chemistry_12
    agent_mapping.update({
        '12 chemistry': chemistry_12, 'class 12 chemistry': chemistry_12
    })
    print("✓ Chemistry 12 imported")
except ImportError as e:
    print(f"✗ Chemistry 12 import failed: {e}")

try:
    from class_12.botany_quiz_system_12.botany_quiz_agent_12 import botany_quiz_agent_12 as botany_12
    agent_mapping.update({
        '12 botany': botany_12, 'class 12 botany': botany_12
    })
    print("✓ Botany 12 imported")
except ImportError as e:
    print(f"✗ Botany 12 import failed: {e}")
# FIXED: Zoology 12 - Correct file name
try:
    from class_12.zoology_quiz_system_12.zoology_quiz_agent_12 import zoology_quiz_agent_12 as zoology_12
    agent_mapping.update({
        '12 zoology': zoology_12, 'class 12 zoology': zoology_12
    })
    print("✓ Zoology 12 imported")
except ImportError as e:
    print(f"✗ Zoology 12 import failed: {e}")

# FIXED: Computer 12 - Correct file name
try:
    from class_12.computer_quiz_system_12.computer_quiz_agent_12 import computer_quiz_agent_12 as computer_12
    agent_mapping.update({
        '12 computer': computer_12, 'class 12 computer': computer_12, '12 cs': computer_12
    })
    print("✓ Computer 12 imported")
except ImportError as e:
    print(f"✗ Computer 12 import failed: {e}")

try:
    from class_12.english_quiz_system_12.english_quiz_agent_12 import english_quiz_agent_12 as english_12
    agent_mapping.update({
        '12 english': english_12, 'class 12 english': english_12
    })
    print("✓ English 12 imported")
except ImportError as e:
    print(f"✗ English 12 import failed: {e}")

print(f"\n✅ Total agents loaded: {len(agent_mapping) - 1}")  # Subtract config
print("Available subjects:", [k for k in agent_mapping.keys() if k != 'config'])

# Keep the original main function for CLI use
async def main():
    print("\n🎓 Direct Agent Access System")
    print("📚 Available: Class 9/10/11/12 - Math, Physics, Chemistry, Biology, Botany, Zoology, Computer, English")
    print("💡 Examples: 'class 9 math', '11 physics', '12 chemistry', 'biology class 10', '11 botany'")
    print("❌ Type 'exit' to quit\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ["exit", "quit", "bye"]:
            print("👋 Goodbye!")
            break
        
        # Find the right agent
        selected_agent = None
        selected_key = None
        
        for key, agent in agent_mapping.items():
            if key != 'config' and key in user_input:
                selected_agent = agent
                selected_key = key
                break
        
        if selected_agent:
            print(f"🔍 Selected: {selected_key.upper()}")
            print("📄 Generating paper...\n" + "="*50)
            
            try:
                agent_response = Runner.run_streamed(
                    selected_agent,
                    input="Generate a comprehensive target paper for 2025",
                    run_config=config
                )
                
                async for event in agent_response.stream_events():
                    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                        print(event.data.delta, end="", flush=True)
                
                print("\n" + "="*50)
                print("✅ Paper generated successfully!")
                
            except Exception as e:
                print(f"❌ Error generating paper: {e}")
        else:
            print("❓ Please specify class and subject clearly.")
            print("   Examples: 'class 9 math', '11 physics', '12 chemistry', 'biology class 10', '11 botany'")
            print("   Available:", [k for k in agent_mapping.keys() if k != 'config'])

if __name__ == "__main__":
    asyncio.run(main())