import random
player_nexus_health = 30
cpu_nexus_health = 30
player_barrier_points = 0
cpu_barrier_points = 0
attack_array = 6
cpu_attack_points = []
gameRunning = True
turn = "Player"
round = 1

while gameRunning:
    if cpu_nexus_health <= 0:
        print(cpu_nexus_health)
        print("Congratz, you win!")
        gameRunning = False
        break
    elif player_nexus_health <= 0:
        print("You lose :(")
        gameRunning = False
        break
    print("\n------ ROUND " + str(round) + "------")
    print(f"HP: {str(player_nexus_health):>8}")
    print(f"Enemy HP: {str(cpu_nexus_health)}")
    while turn == "Player":
        player_attack_points = []
        i = 0
        for i in range(6): #Total de ataque
            random_value = random.randint(0, 3)
            player_attack_points.append(random_value)
        print("\nTotal de ataque: " + str(sum(player_attack_points)) +". Tentar outra? s/n") # Termina total de ataque
        print([player_attack_points])
        retry = input("")
        if retry == "n":
            print("\nVida inimiga: " + str(cpu_nexus_health))
            cpu_nexus_health = cpu_nexus_health - sum(player_attack_points)
            turn = "CPU"
    while turn == "CPU":
        cpu_attack_points = []
        for i in range(6):
            cpu_random_value = random.randint(1, 3)
            cpu_attack_points.append(cpu_random_value)
        player_nexus_health = player_nexus_health - sum(cpu_attack_points)
        print("Você tomou " + str(sum(cpu_attack_points)) + " de dano. Vida atual: " + str(player_nexus_health))
        round += 1
        turn = "Player"