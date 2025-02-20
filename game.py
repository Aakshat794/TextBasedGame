
def char():
    return {"hp": 100, "atk": 10, "def": 5, "lvl": 1, "xp": 0, "pot": 3}

def enemy(lvl):
    return {"hp": 50 + lvl * 10, "atk": 5 + lvl * 2, "def": 3 + lvl, "xp": 20 * lvl}


def battle(p, e):
    while p["hp"] > 0 and e["hp"] > 0:
        print(f"HP: {p['hp']} | Enemy HP: {e['hp']}")
        c = input("(A)ttack (D)efend (H)eal: ").lower()
        if c == "a":
            dmg = max(1, p["atk"] - e["def"])
            e["hp"] -= dmg
            print(f"You hit for {dmg} damage!")
        elif c == "d":
            print("You brace for impact!")
            p["def"] += 2
        elif c == "h" and p["pot"] > 0:
            p["hp"] += 20
            p["pot"] -= 1
            print("You healed 20 HP!")
        if e["hp"] > 0:
            dmg = max(1, e["atk"] - p["def"])
            p["hp"] -= dmg
            print(f"Enemy hits for {dmg} damage!")
    return p["hp"] > 0


def lvl_up(p):
    if p["xp"] >= 100:
        p["lvl"] += 1
        p["xp"] = 0
        p["atk"] += 5
        p["def"] += 3
        p["hp"] = 100
        print("You leveled up!")


def game():
    p = char()
    while p["hp"] > 0:
        e = enemy(p["lvl"])
        print("A wild enemy appears!")
        if battle(p, e):
            print("You won!")
            p["xp"] += e["xp"]
            lvl_up(p)
        else:
            print("Game Over!")
            break

game()
