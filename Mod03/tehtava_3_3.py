suorakulmio_kanta_input = input("Anna suorakulmion kanta: ")
suorakulmio_korkeus_input = input("Anna suorakulmion korkeus: ")
suorakulmio_kanta = float(suorakulmio_kanta_input)
suorakulmio_korkeus = float(suorakulmio_korkeus_input)

print(f"Suorakulmion piiri on: {(suorakulmio_kanta+suorakulmio_korkeus)*2}")
print(f"Suorakulmion pinta-ala on: {suorakulmio_kanta*suorakulmio_korkeus:.2f}")

