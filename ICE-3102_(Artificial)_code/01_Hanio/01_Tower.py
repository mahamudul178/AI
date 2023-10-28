
def tower_of_hanio(n, from_rod, to_rod, aux_rod):
    if n==1:
        print("Move disk 1 from rod", from_rod, "to_rod", to_rod)
        return
    tower_of_hanio(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from_rod", from_rod, "to_rod",to_rod)
    tower_of_hanio(n-1, aux_rod, to_rod, from_rod)

n=int(input("Enter number of disk: "))
tower_of_hanio(n,'A','C', 'B')