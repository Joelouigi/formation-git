
# engine.py
# Gestion très basique d'un moteur

def start_engine():
    print("🔑 Mise en marche du moteur...")
    return True

def stop_engine():
    print("🛑 Arrêt du moteur...")
    return False

def engine_status(running: bool):
    print(f'is it running: {running}') 

def boost_engine(): 
    print("💨 Mode turbo activé !") 
