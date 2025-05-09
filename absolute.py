from bench_runner import result

head = result.Result.from_arbitrary_filename("TC-PGO-Ex2.json")
base = result.Result.from_arbitrary_filename("PGO.json")

head_timing_data = head.get_timing_data()
base_timing_data = base.get_timing_data()

with open("absolute.csv", "w") as f:
    f.write("benchmark,default,tail-calling,ratio\n")
    for bm, head_values in sorted(head_timing_data.items()):
        if bm not in base_timing_data:
            continue
        base_values = base_timing_data[bm]
        f.write(
            f"{bm},{base_values.mean()},{head_values.mean()},{head_values.mean()/base_values.mean()}\n"
        )
