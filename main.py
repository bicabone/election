from simulation import Simulation, Party

if __name__ == "__main__":
    sim = Simulation()
    d = {Party.RED: 0, Party.BLUE: 0, Party.COMMUNIST: 0}
    for i in range(1000000):
        winner = sim.run("Donald Trump")
        d[winner] += 1
        if i % 10000 == 1:
            print(f"Intermediate {d}")
    print(d)
