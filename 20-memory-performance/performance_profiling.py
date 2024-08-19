import cProfile
import pstats
import io

def compute_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

def main():
    result = compute_sum(100000)
    print(f"Sum is {result}")

if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    
    main()
    
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    
    print(s.getvalue())
