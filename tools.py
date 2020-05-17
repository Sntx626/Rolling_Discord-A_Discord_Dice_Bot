import json
import datetime

with open("config.json") as f:
    config = json.load(f)
    command_prefix = config["command prefix"]
    name_suffix = config["results suffix"]

with open("results/results_"+ name_suffix +".json") as f:
    results = json.load(f)

def print_on_command_call(ctx_author, command_name, input):
    print(f"\n{ctx_author} '{command_prefix}{command_name} {input}':")

def print_bot(output, ctx_author, command_name, input):
    print(output)
    add_results_entry(f"\n{ctx_author} '{command_prefix}{command_name} {input}':", output)

def add_results_entry(input, output):
    with open("results/results_"+name_suffix+".json") as f:
        data = json.load(f)
    
    result = {
    "input":input,
    "output":output,
    "timestamp":datetime.datetime.now().strftime("%c")
    }
    
    data.append(result)
    with open("results/results_"+name_suffix+".json", 'w') as f:
        json.dump(data, f, indent=2)