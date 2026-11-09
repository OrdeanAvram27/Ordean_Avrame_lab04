def este_prim(n):
    """Verifică dacă un număr n este prim fără biblioteci externe."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def goldbach(n):
    """Găsește toate perechile (p, q) de numere prime unde p + q = n și p <= q."""
    perechi = []
    for p in range(2, n // 2 + 1):
        if este_prim(p):
            q = n - p
            if este_prim(q):
                perechi.append((p, q))
    return perechi

def main():
    date_intrare = input("Introduceți un număr natural par (> 2): ").strip()
    
    # Validare date de intrare
    if not date_intrare.isdigit():
        print("Eroare: Valoarea introdusă nu este un număr natural valid!")
        return
    
    n = int(date_intrare)
    
    if n <= 2:
        print("Eroare: Numărul trebuie să fie strict mai mare decât 2!")
        return
    
    if n % 2 != 0:
        print("Eroare: Numărul trebuie să fie par!")
        return

    rezultate = goldbach(n)
    
    if rezultate:
        print(f"Descompunerile Goldbach pentru {n} sunt:")
        for p, q in rezultate:
            print(f"{n} = {p} + {q}")
    else:
        print("Nu s-au găsit descompuneri.")

if __name__ == "__main__":
    main()