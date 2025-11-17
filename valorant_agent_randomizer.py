import random

agents = [
    "Astra", "Breach", "Brimstone", "Chamber", "Clove", "Cypher", "Deadlock", "Fade", "Gekko", "Harbor",
    "Iso", "Jett", "KAY/O", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", 
    "Sova", "Tejo", "Veto", "Viper", "Vyse", "Waylay", "Yoru"
]

num = random.randint(0, 26)
print(f'Random number: {num}')
print(agents[num])