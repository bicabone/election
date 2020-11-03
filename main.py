from simulation import Simulation, Party

if __name__ == "__main__":
    sim = Simulation()
    d = {Party.RED: 0, Party.BLUE: 0, Party.COMMUNIST: 0}
    for i in range(1000000):
        if i % 10000 == 0:
            print(f"Intermediate {d}")
        winner = sim.run("Donald Trump")
        d[winner] += 1

    print(d)
