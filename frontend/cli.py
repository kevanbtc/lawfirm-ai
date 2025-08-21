import argparse
from agents.research_agent import ResearchAgent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", required=True, choices=["research"])
    parser.add_argument("--option", required=True, help="Query to run")
    parser.add_argument("--model", default="gpt-4o")
    parser.add_argument("--temperature", type=float, default=0.7)
    args = parser.parse_args()

    if args.agent == "research":
        agent = ResearchAgent(model_name=args.model, temperature=args.temperature)
        result = agent.run(args.option)
        print(result)


if __name__ == "__main__":
    main()
